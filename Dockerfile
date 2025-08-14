FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY main.py ./
COPY src/ ./src/

ENTRYPOINT ["uv", "run", "python", "main.py"]
