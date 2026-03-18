#!/bin/bash

# Travel Agent Deployment Script
# Run this on the e2-micro VM

set -e

echo "=== Travel Agent Deployment ==="

# Navigate to app directory
cd /home/$USER/travel-agent 2>/dev/null || cd "$(dirname "$0")"

# Pull latest changes
echo "Pulling latest changes..."
git pull origin main

# Build and start the container
echo "Building and starting Docker container..."
docker-compose build
docker-compose up -d

echo "=== Deployment Complete ==="
echo "App running on port 80"
echo "Backend API at http://<your-ip>/api/"
