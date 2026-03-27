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
