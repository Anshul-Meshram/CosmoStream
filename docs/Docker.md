# Docker Notes

## Image

A Docker image is a read-only template used to create containers. It contains the application code, dependencies, runtime, and configuration required to run an application.

In CosmoStream, each major component (backend, frontend, and gateway) will eventually have its own Docker image.

---

## Container

A container is a running instance of a Docker image.

Containers are isolated from one another, allowing each service to run independently while sharing the host operating system's kernel.

---

## Dockerfile

A Dockerfile is a set of instructions that defines how a Docker image is built.

Each service in CosmoStream will have its own Dockerfile so that it can be built, tested, and deployed independently.

---

## Docker Compose

Docker Compose is a tool for defining and running multiple containers using a single configuration file (`compose.yaml`).

Instead of starting each container manually, Compose manages the entire application stack.

### Key Concepts

- Services
- Networks
- Volumes
- Environment Variables
- Build Context

### Common Commands

```bash
docker compose up
docker compose down
docker compose ps
docker compose logs
docker compose restart
```

---

## Why Multiple Services?

CosmoStream follows a microservices-inspired architecture where the backend, frontend, and gateway are developed as separate services.

### Backend

Contains the core application logic, APIs, data processing, authentication, and communication with databases and external services.

### Frontend

Provides the user interface. It communicates with the backend through APIs and implements features such as Role-Based Access Control (RBAC) for different user roles like administrators and developers.

### Gateway

Acts as the entry point between clients and backend services. It receives incoming requests, forwards them to the appropriate service, and can later handle authentication, routing, rate limiting, and load balancing.

---

## Why Separate Docker Images?

Each service has its own Docker image because they have different responsibilities and dependencies.

Separating them allows us to:

- Build each service independently.
- Test services without affecting others.
- Deploy updates to one service without rebuilding the entire system.
- Scale services independently as the project grows.
- Maintain a modular and easier-to-manage architecture.
