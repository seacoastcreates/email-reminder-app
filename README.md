# fastapi-temporal-app

A FastAPI + Temporal example app for orchestrating email reminder workflows.

---

## Key Components

### 1. FastAPI Server (`main.py`)

- Exposes an HTTP API endpoint:
  - `POST /send-email/` — Starts an email reminder workflow for the provided email address.
- On startup, connects to the Temporal server using `wait_for_temporal()`.

### 2. Temporal Client

- The FastAPI app uses the Temporal Python SDK to connect to the Temporal server (running in Docker, see `docker-compose.yml`).
- When you call `/send-email/`, it starts a workflow named `"email-reminder-workflow"` on the `"email-task-queue"`.

### 3. Worker (`worker.py`)

- Runs as a separate process/service.
- Registers the workflow (`EmailReminderWorkflow`) and activity (`send_email_activity`) with Temporal.
- Listens on the `"email-task-queue"` for new workflow tasks and executes them.

### 4. Docker Compose (`docker-compose.yml`)

- Orchestrates the following services:
  - **Postgres**: Database for Temporal.
  - **Temporal**: The Temporal server.
  - **fastapi**: The FastAPI API server.
  - **worker**: The Temporal worker process.

### 5. Connection Handling (`utils.py`)

- `wait_for_temporal()` tries to connect to the Temporal server, retrying until it’s ready.

---

## How a Request Flows

1. **User sends a POST request to `/send-email/` with an email address.**
2. **FastAPI** receives the request and uses the Temporal client to start a new workflow instance.
3. **Temporal server** queues the workflow task on `"email-task-queue"`.
4. **Worker** picks up the task, runs the workflow logic (e.g., sends an email).
5. **FastAPI** responds with the workflow and run IDs, or an error if something goes wrong.

---

## Summary

- **FastAPI** = API gateway for workflow requests.
- **Temporal** = Orchestrates and manages workflow execution.
- **Worker** = Executes the actual workflow logic.
- **Docker Compose** = Runs everything together for local development.
