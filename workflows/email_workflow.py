from temporalio import workflow
from workflows.activities import send_email_activity

@workflow.defn
class EmailReminderWorkflow:
    @workflow.run
    async def run(self, email: str):
        workflow.logger.info(f"Starting email reminder workflow for {email}")
        # Call the activity to send an email
        await workflow.execute_activity(
            send_email_activity,
            email,
            start_to_close_timeout=timedelta(seconds=10)
        )
        workflow.logger.info(f"Email reminder workflow completed for {email}")