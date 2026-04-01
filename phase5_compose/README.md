# Phase 5 & 6: Multi-Container Networking & Docker Hub

This project demonstrates a production-grade local development environment using Docker Compose.

## Architecture
- **Web Tier:** Python 3.9-slim (Flask)
- **Data Tier:** Redis (Alpine)
- **Networking:** Private Docker Bridge Network
- **Persistence:** Docker Managed Volume (redis_data)

## Key Commands Used
- docker-compose up --build -d
- docker-compose restart web-app
- docker-compose down
- docker login
- docker tag [ID] arunmxbox/my-python-app:v1.0
- docker push arunmxbox/my-python-app:v1.0

## Results
The application successfully tracks page views. Even after running docker-compose down, the view count is preserved thanks to the persistent Volume mapping.

**Docker Hub Image:** https://hub.docker.com/r/arunmxbox/my-python-app
