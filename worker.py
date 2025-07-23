import asyncio
from temporalio.worker import Worker
from workflows.email_workflow import EmailReminderWorkflow
from workflows.activities import send_email_activity
from temporalio.client import Client
from utils import wait_for_temporal

async def main():
    # Connect to the Temporal server
    client = await wait_for_temporal()

    # Create a worker to handle the email reminder workflow and activities
    worker = Worker(
        client,
        task_queue="email-task-queue",
        workflows=[EmailReminderWorkflow],
        activities=[send_email_activity],
    )

    # Start the worker
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())