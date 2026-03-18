#!/bin/bash

# Travel Agent Deployment Script
# Run this on the e2-micro VM

set -e

echo "=== Travel Agent Deployment ==="

# Navigate to app directory (adjust path as needed)
cd /home/$USER/travel-agent 2>/dev/null || cd "$(dirname "$0")"

# Pull latest changes
echo "Pulling latest changes..."
git pull origin main

# Build and start the container
echo "Building and starting Docker container..."
docker-compose build backend
docker-compose up -d backend

echo "=== Deployment Complete ==="
echo "Backend running on port 5000"
