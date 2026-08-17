FROM node:22-alpine AS frontend-builder

WORKDIR /build

COPY package*.json ./
RUN npm ci

RUN npm install @hexlet/project-devops-deploy-crud-frontend

RUN mkdir -p /build/public
RUN cp -r ./node_modules/@hexlet/project-devops-deploy-crud-frontend/dist/. /build/public/

FROM python:3.12-slim AS base

RUN apt-get update && \
    apt-get install -y nginx libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY app ./app
COPY --from=frontend-builder /build/public /app/public
COPY nginx.conf /etc/nginx/nginx.conf

ENV PORT=8080
ENV DATABASE_URL=""

CMD sh -c "uv run uvicorn app.main:app --host 0.0.0.0 --port 8080 & nginx -g 'daemon off;'"
