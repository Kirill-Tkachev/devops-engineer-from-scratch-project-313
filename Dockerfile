FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y nginx curl libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY package*.json ./
RUN npm install

COPY . .

RUN mkdir -p /app/public
RUN cp -r ./dist/. /app/public/

COPY nginx.conf /etc/nginx/nginx.conf

CMD sh -c "uv run uvicorn app.main:app --host 0.0.0.0 --port 8080 & nginx -g 'daemon off;'"