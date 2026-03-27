# 🐳 Docker Mastery - Day 1: Command Log
**User:** Arun Kumar | **Topic:** Container Lifecycle & Troubleshooting

| Command | Why we used it |
| :--- | :--- |
| `docker images` | To audit existing blueprints on the MacBook Air. |
| `docker ps -a` | To see ALL containers (Running + Exited). Essential for finding name conflicts. |
| `docker run -it` | To enter the "Interactive" Linux environment inside a container. |
| `docker rm <name>` | To delete an exited container and free up the name/resources. |
| `docker system prune -f` | The "Deep Clean" - deletes all stopped containers and unused cache. |
| `docker run --rm` | The "Master Move" - automatically deletes the container upon exit. |

**Key Lesson:** A container being "Exited" is not the same as being "Deleted."

## Phase 2: Port Mapping (The Bridge)
| Command Flag | Why we used it |
| :--- | :--- |
| `-d` | To run the container in the background (Detached). |
| `-p 8888:8000` | To map the MacBook's port 8888 to the Container's port 8000. |
| `localhost:8888` | The address used in the browser to reach the isolated container. |

**Key Lesson:** Without the -p flag, the container is invisible to the outside world.
