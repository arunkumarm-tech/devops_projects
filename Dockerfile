# 1. Use a lightweight Python base
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy our website file from the Mac into the Container
COPY my_website_data/index.html .

# 4. Tell the container to start the web server on port 8000
CMD ["python3", "-m", "http.server", "8000"]
