import createClient, { type Middleware } from 'openapi-fetch';

import type { paths } from './types';
import { retryFetch } from './retry-fetch';

type OAuthTokenResponse = {
	access_token: string;
	token_type: string;
	expires_in?: number;
	scope?: string;
};

export type Config = {
	tokenUrl: string;
	serverUrl: string;
	clientId?: string;
	clientSecret?: string;
	scopes?: string[];
};

export const ProductionConfig: Config = {
	tokenUrl: 'https://api.intra.42.fr/oauth/token',
	serverUrl: 'https://api.intra.42.fr/v2',
};

export const StagingConfig: Config = {
	tokenUrl: 'https://api.intra-staging.42.fr/oauth/token',
	serverUrl: 'https://api.intra-staging.42.fr/v2',
};

export function withClientCredentials(
	config: Config,
	clientId: string,
	clientSecret: string
): Config {
	return {
		...config,
		clientId,
		clientSecret,
	};
}

export function withScopes(config: Config, ...scopes: string[]): Config {
	return {
		...config,
		scopes,
	};
}

class RefreshableTokenSource {
	private accessToken?: string;
	private expiresAt = 0;
	private pendingRequest?: Promise<string>;

	constructor(private readonly config: Config) {}

	async token(): Promise<string> {
		const now = Date.now();

		if (this.accessToken !== undefined && now < this.expiresAt - 60_000) {
			return this.accessToken;
		}

		if (this.pendingRequest !== undefined) {
			return this.pendingRequest;
		}

		this.pendingRequest = this.fetchToken();

		try {
			return await this.pendingRequest;
		} finally {
			this.pendingRequest = undefined;
		}
	}

	invalidate(): void {
		this.accessToken = undefined;
		this.expiresAt = 0;
	}

	private async fetchToken(): Promise<string> {
		if (!this.config.clientId || !this.config.clientSecret) {
			throw new Error('OAuth client credentials are missing');
		}

		const params = new URLSearchParams({
			client_id: this.config.clientId,
			client_secret: this.config.clientSecret,
			grant_type: 'client_credentials',
			scope: this.config.scopes?.join(' ') ?? '',
		});

		const response = await fetch(
			`${this.config.tokenUrl}?${params.toString()}`,
			{
				method: 'POST',
				headers: {
					Accept: 'application/json',
				},
			}
		);

		if (!response.ok) {
			throw new Error(
				`OAuth token request failed: ${response.status} ${await response.text()}`
			);
		}

		const payload = (await response.json()) as OAuthTokenResponse;

		if (!payload.access_token) {
			throw new Error(
				'OAuth token response did not contain access_token'
			);
		}

		this.accessToken = payload.access_token;
		this.expiresAt = Date.now() + (payload.expires_in ?? 3_600) * 1_000;

		return this.accessToken;
	}
}

export function createApiClient(config: Config) {
	const tokenSource = new RefreshableTokenSource(config);

	const client = createClient<paths>({
		baseUrl: config.serverUrl,
		fetch: retryFetch,
	});

	const authMiddleware: Middleware = {
		async onRequest({ request }) {
			const token = await tokenSource.token();

			request.headers.set('Authorization', `Bearer ${token}`);

			return request;
		},

		async onResponse({ request, response }) {
			if (response.status !== 401) {
				return response;
			}

			response.body?.cancel();
			tokenSource.invalidate();

			const retryRequest = request.clone();
			const token = await tokenSource.token();

			retryRequest.headers.set('Authorization', `Bearer ${token}`);

			return retryFetch(retryRequest);
		},
	};

	client.use(authMiddleware);

	return client;
}
