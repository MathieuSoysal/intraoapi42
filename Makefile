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
		-v ./openapi.yaml:/gen/openapi.yaml \
		-v ./redocly.yaml:/redocly.yaml:ro \
		redocly/cli:2.40.0 \
		bundle openapi.yaml --config /redocly.yaml --force --ext yaml -o /gen/openapi.yaml 2> /dev/null

lint:
	docker run --rm --user ${UID}:${GID} \
		-v ./openapi.yaml:/spec/openapi.yaml \
		-v ./redocly.yaml:/redocly.yaml:ro \
		redocly/cli:2.40.0 \
		lint --config /redocly.yaml --lint-config error openapi.yaml 

.PHONY: all indexes bundle