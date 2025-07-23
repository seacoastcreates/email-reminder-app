# FastAPI server

import asyncio
from fastapi import FastAPI
from temporalio.client import Client   
from utils import wait_for_temporal

app = FastAPI()
temporal_client = None

@app.on_event("startup")
async def startup_event():
    global temporal_client
    # Initialize the Temporal client
    temporal_client = wait_for_temporal()

@app.post("/send-email/")
async def send_email(email: str):
    result = await temporal_client.start_workflow(
        "email-reminder-workflow",
        email,
        id=f"workflow-{email}",
        task_queue="email-task-queue"
    )
    return {"workflow_id": result.workflow_id, "run_id": result.run_id}