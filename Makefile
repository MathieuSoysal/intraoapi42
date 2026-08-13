OPENAPI_SPEC := openapi.yaml

all: indexes bundle lint

indexes:
	# we need to install the python deps (tool/requirements.txt) and run tool/generate_indexes.py
	docker run --rm --user ${UID}:${GID} \
		-w / \
		-v ./specs:/specs \
		-v ./tool:/tool \
		python:3.11-slim \
		bash -c "pip install -r /tool/requirements.txt && python /tool/generate_indexes.py"

bundle:
	docker run --rm --user ${UID}:${GID} \
		-v ./specs:/spec \
		-v ./$(OPENAPI_SPEC):/gen/$(OPENAPI_SPEC) \
		-v ./redocly.yaml:/redocly.yaml:ro \
		redocly/cli:2.40.0 \
		bundle $(OPENAPI_SPEC) --config /redocly.yaml --force --ext yaml -o /gen/$(OPENAPI_SPEC) 2> /dev/null

lint:
	docker run --rm --user ${UID}:${GID} \
		-v ./$(OPENAPI_SPEC):/spec/$(OPENAPI_SPEC) \
		-v ./redocly.yaml:/redocly.yaml:ro \
		redocly/cli:2.40.0 \
		lint --config /redocly.yaml --lint-config error $(OPENAPI_SPEC)

generate-python:
	docker run --rm \
		--user "$$(id -u):$$(id -g)" \
		-v "$(CURDIR):/workspace" \
		--workdir /workspace \
		--entrypoint openapi-python-client \
		openapi-python-client:local \
		generate \
		--path "/workspace/$(OPENAPI_SPEC)" \
		--config /workspace/clients/python/config.yaml \
		--output-path /workspace/clients/python/intraoapi42 \
		--overwrite

generate-go:
	cd clients/go && go generate ./...

generate-typescript:
	cd clients/typescript && npm run generate:api

generate-clients: generate-go generate-python generate-typescript

docs:
	docker compose \
		-f docs/docker-compose.yml \
		up

.PHONY: all indexes bundle docs generate-python generate-go