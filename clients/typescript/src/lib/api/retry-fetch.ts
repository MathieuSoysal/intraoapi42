const RATE_LIMIT_RETRY_DELAY = 1_000;
const RATE_LIMIT_MAX_RETRIES = 3;

const SERVER_ERROR_RETRY_DELAY = 500;
const SERVER_ERROR_MAX_RETRIES = 5;

function sleep(milliseconds: number): Promise<void> {
	return new Promise((resolve) => {
		setTimeout(resolve, milliseconds);
	});
}

export async function retryFetch(
	input: RequestInfo | URL,
	init?: RequestInit
): Promise<Response> {
	let rateLimitAttempts = 0;
	let serverErrorAttempts = 0;

	const originalRequest = new Request(input, init);

	while (true) {
		const request = originalRequest.clone();
		const response = await fetch(request);

		if (
			response.status === 429 &&
			rateLimitAttempts < RATE_LIMIT_MAX_RETRIES
		) {
			rateLimitAttempts++;

			await response.arrayBuffer();
			await sleep(RATE_LIMIT_RETRY_DELAY);

			continue;
		}

		if (
			response.status === 500 &&
			serverErrorAttempts < SERVER_ERROR_MAX_RETRIES
		) {
			serverErrorAttempts++;

			await response.arrayBuffer();
			await sleep(SERVER_ERROR_RETRY_DELAY);

			continue;
		}

		return response;
	}
}
