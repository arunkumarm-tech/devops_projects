# Phase 5 & 6: Multi-Container Networking & Cloud Registry

This project demonstrates a production-ready Docker setup using a Python Flask application and a Redis database.

## Architecture
- **Web App:** Python 3.9-slim running Flask.
- **Database:** Redis (Alpine-based) for high-speed in-memory caching.
- **Persistence:** Docker Volumes are used to ensure Redis data survives container restarts.
- **Networking:** Docker Compose creates a private virtual network for secure service-to-service communication.

## Features
- **Hot Reloading:** Bind mounts allow for real-time code changes.
- **Data Persistence:** Managed volumes prevent data loss.
- **Registry:** Image is pushed to Docker Hub for cloud deployment.

## How to Run
1. Clone the repo.
2. Run `docker-compose up -d`.
3. Access at `http://localhost:5001`.

## Docker Hub
The image is available at: [hub.docker.com/r/arunmxbox/my-python-app](https://hub.docker.com/r/arunmxbox/my-python-app)
