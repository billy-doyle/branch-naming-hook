export UV_PYTHON := 3.13
export UV_PYTHON_PREFERENCE := only-managed

install:
	@which uv > /dev/null && echo "uv is already installed." || { \
	    echo "uv is not installed. Installing..."; \
	    curl -LsSf https://astral.sh/uv/install.sh | sh; \
		exec $0; \
	}
	@uv python install ${UV_PYTHON}
	@uv venv --allow-existing
	@uv sync --extra dev
	@uv run python -m pre_commit install

tests:
	@uv run python -m unittest discover

lint:
	@uv run python -m pre_commit run --all-files

.PHONY: install tests lint
