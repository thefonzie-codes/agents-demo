# syntax=docker/dockerfile:1

# Stage 1: Build React frontend
FROM node:20-alpine AS frontend-builder

WORKDIR /frontend

# Copy frontend files
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend/src ./src
COPY frontend/index.html ./
COPY frontend/public ./public
COPY frontend/vite.config.ts ./
COPY frontend/tsconfig*.json ./
COPY frontend/eslint.config.js ./
# COPY frontend/.env ./

RUN npm run build

# Stage 2: Python backend
FROM python:3.11-slim

WORKDIR /app

# Install nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Copy backend files
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/

# Copy built frontend to nginx directory
COPY --from=frontend-builder /frontend/dist /var/www/html

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Environment variables
ENV FLASK_APP=backend/app.py
ENV PYTHONUNBUFFERED=1
ENV FLASK_RUN_HOST=127.0.0.1

EXPOSE 80

# Start nginx and gunicorn via supervisord
RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
