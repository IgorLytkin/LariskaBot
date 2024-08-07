FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container to /LariskaBot
WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Add the current directory contents into the container at /LariskaBot
COPY . /app
CMD ["python", "-m", "main"]

# -------------------------------
# Build an image from a Dockerfile:
# $ docker build -t lariska_bot .
# -------------------------------
# Create and run a new container from an image:
# $ docker run -d --name LariskaBot \
#    --env "BOT_TOKEN=<BOT_TOKEN>" \
#    --env "AI_KEY=<AI_KEY>" \
#    --env "VCHAT_ID=<VCHAT_ID>" \
#    --env "DCHAT_ID=<DCHAT_ID>" \
#    --env "SCHAT_ID=<SCHAT_ID>" \
#    lariska_bot
# -------------------------------
# Stop running container:
# $ docker stop LariskaBot
# -------------------------------
# Start stopped container:
# $ docker start LariskaBot
# -------------------------------
# Remove container:
# $ docker rm LariskaBot
# -------------------------------
# Remove image:
# $ docker rmi lariska_bot
# -------------------------------
# Execute a command in a running container:
# $ docker exec -it LariskaBot bash
