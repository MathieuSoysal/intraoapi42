# intraoapi42

A Go client for the [42 Intranet API](https://api.intra.42.fr), generated from an OpenAPI 3 description with [oapi-codegen](https://github.com/oapi-codegen/oapi-codegen), plus a thin wrapper handling OAuth2 client-credentials auth and automatic retries.

> ⚠️ **Unofficial spec.** The OpenAPI description in this repo is **not** provided by 42. It has been hand-crafted from the public [`api.intra.42.fr/apidoc`](https://api.intra.42.fr/apidoc) reference and from observing real responses. Coverage of the full API surface is currently partial, **contributions are very welcome**, see [Contributing](#contributing).

> 💡 **Not a Go user?** The bundled [`openapi.yaml`](./openapi.yaml) is a standard, self-contained OpenAPI 3 document, it isn't tied to `oapi-codegen` or to Go. You can feed it into any other client generator (e.g. [openapi-generator](https://openapi-generator.tech/), [openapi-python-client](https://github.com/openapi-generators/openapi-python-client), Swagger Codegen, etc.) to produce a client in Python, TypeScript, Java, Rust, or whatever language you need. See [Using the spec in other languages](#using-the-spec-in-other-languages).

## Features

- Strongly-typed request/response models generated straight from the OpenAPI spec (`ClientWithResponses`)
- OAuth2 client-credentials flow with automatic, cached, thread-safe token refresh
- Built-in retry transport for rate limiting, transient server errors, and expired tokens
- Spec split into small, per-resource YAML files under `specs/`, bundled and linted with [Redocly CLI](https://redocly.com/docs/cli)
- The bundled `openapi.yaml` is plain OpenAPI 3, language-agnostic, so it can drive client generation for Python, TypeScript, or any other language, not just this Go package

## Installation

```bash
go get github.com/42paris/intraoapi42
```

## Quick start

```go
package main

import (
	"context"
	"fmt"
	"log"

	intraoapi42 "github.com/42paris/intraoapi42"
)

func main() {
	ctx := context.Background()

	config := intraoapi42.ProductionConfig.
		WithClientCredentials("your-client-id", "your-client-secret").
		WithScopes("public")

	client, err := intraoapi42.New(config)
	if err != nil {
		log.Fatal(err)
	}

	resp, err := client.GetUsersWithResponse(ctx, &intraoapi42.GetUsersParams{})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(resp.StatusCode())
}
```

> The exact generated method and parameter names (`Get...WithResponse`, `...Params`, etc.) come from the `operationId`s defined under `specs/paths/` and live in `openapi.gen.go`. Browse that file (or run `go doc github.com/42paris/intraoapi42`) for the full list of currently available endpoints, it will grow as the spec gets more complete.

## Using the spec in other languages

This repo's real deliverable is arguably the spec itself: `openapi.yaml` at the repo root is a fully bundled, single-file OpenAPI 3 description with no external `$ref`s left to resolve. It has no dependency on Go or on `oapi-codegen`, so it works as input to any OpenAPI-compatible generator. For example:

```bash
# Python (openapi-python-client)
pip install openapi-python-client
openapi-python-client generate --url https://raw.githubusercontent.com/42paris/intraoapi42/main/openapi.yaml

# Any language, via the generic openapi-generator (needs Java)
npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g python \
  -o ./client-python
# swap "-g python" for "-g typescript-fetch", "-g java", "-g rust", etc.
```

A few things worth knowing if you go this route:

- Always generate from the bundled `openapi.yaml`, not from files under `specs/`, those are hand-maintained fragments meant to be assembled by `make bundle` and aren't valid standalone specs.
- Since the spec is hand-crafted and partial (see the note at the top of this README), coverage and accuracy for generators other than `oapi-codegen` haven't been verified as thoroughly, please report issues, they most likely mean the spec needs fixing rather than the generator.
- OAuth2 client-credentials handling, retries, and pagination helpers are specific to this Go package, generators for other languages will only give you the typed request/response models and raw HTTP calls, you'll need to write the equivalent auth/retry glue yourself.

## Retry mechanism

`New(config)` wires up an HTTP client with two layered `http.RoundTripper`s:

1. **`oauth2.Transport`**, injects the `Authorization: Bearer <token>` header, backed by a `refreshableTokenSource` that caches the token in memory (guarded by a mutex) and only hits the token endpoint again once the cached token is invalid or expired.
2. **`retryTransport`**, wraps the above and retries the request based on the response status:

| Status                      | Behavior                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `429 Too Many Requests`     | Retried up to **3** times, waiting **1s** between attempts                                                   |
| `500 Internal Server Error` | Retried up to **5** times, waiting **500ms** between attempts                                                |
| `401 Unauthorized`          | The cached token is invalidated (forcing a fresh token fetch on the next attempt) and the request is retried |

## Repository layout

```
.
├── client.go                # Config, New(), retry transport, token source
├── time.go                  # custom time handling for the intra API's date/time formats
├── generate.go              # go:generate directive driving oapi-codegen
├── openapi.gen.go           # generated Go client (do not edit by hand)
├── openapi.yaml             # bundled, single-file OpenAPI spec (generated, do not edit by hand)
├── specs/                   # hand-maintained OpenAPI spec, split by concern
│   ├── openapi.yaml         # spec root, references the folders below
│   ├── paths/               # one file per resource/endpoint group
│   ├── schemas/             # one file per data model
│   └── parameters/          # shared/reusable parameters (e.g. pagination)
└── tool/
    ├── generate_indexes.py  # regenerates each specs/*/_index.yaml
    └── requirements.txt
```

Each folder under `specs/` (`paths`, `schemas`, `parameters`) has an auto-generated `_index.yaml` that aggregates every top-level key defined in that folder into `$ref` entries, so the root spec can reference the whole folder without listing every file by hand. **Never edit `_index.yaml` files directly**, they're regenerated by `tool/generate_indexes.py`.

## Working on the spec

The Makefile drives the whole spec pipeline (Docker is the only local dependency, no need to install Python or Node yourself):

```bash
make indexes   # regenerate specs/{paths,schemas,parameters}/_index.yaml
make bundle    # bundle specs/openapi.yaml + all $refs into ./openapi.yaml
make lint      # lint ./openapi.yaml with redocly/cli
make all       # runs the three steps above, in order
```

Once `openapi.yaml` is up to date, regenerate the Go client bindings:

```bash
go generate ./...   # runs generate.go, invoking oapi-codegen against openapi.yaml
go build ./...
```

`oapi-codegen` is declared as a Go **tool dependency** in `go.mod` (`tool github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen`), so `go generate` can invoke it via `go tool` without a separate global install.

If you're generating a client for a different language instead, you only need `make all` to produce an up-to-date `openapi.yaml`, then point your generator of choice at it as shown in [Using the spec in other languages](#using-the-spec-in-other-languages).

## Contributing

This client is only as good as the spec behind it, and the spec is currently incomplete, plenty of endpoints, schemas, and edge cases from the real 42 API aren't described yet. Contributions of any size are welcome, especially:

- New or missing `paths` (endpoints) and `schemas` (models)
- Corrections to existing schemas: wrong types, missing `required`/nullable fields, incomplete enums
- Better-documented error responses
- Usage examples and documentation improvements

### How to contribute

1. Fork the repo and create a branch.
2. Add or edit YAML under `specs/paths/`, `specs/schemas/`, or `specs/parameters/`, one file per resource, mirroring the existing style. Don't hand-edit `_index.yaml` or the root `openapi.yaml`.
3. Run `make all` to regenerate the indexes, rebuild the bundled `openapi.yaml`, and lint it, fix any lint errors before opening a PR.
4. Run `go generate ./...` and confirm `go build ./...` / `go vet ./...` still pass.
5. Open a PR describing which endpoint(s)/schema(s) you added or changed, and how you verified them against the real API (a sample response, a link into the [apidoc](https://api.intra.42.fr/apidoc), etc.), since the spec is hand-crafted, this kind of provenance is what keeps it trustworthy.