# FastAPI server

import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from temporalio.client import Client
from utils import wait_for_temporal

app = FastAPI()
temporal_client = None

# Define the request body model
class EmailRequest(BaseModel):
    email: str

@app.on_event("startup")
async def startup_event():
    global temporal_client
    temporal_client = await wait_for_temporal()

@app.post("/send-email/")
async def send_email(request: EmailRequest):
    try:
        result = await temporal_client.start_workflow(
            "email-reminder-workflow",
            request.email,
            id=f"workflow-{request.email}",
            task_queue="email-task-queue"
        )
        return {"workflow_id": result.id, "run_id": result.first_run_id}
    except Exception as e:
        return {"error": str(e)}
