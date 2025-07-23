from temporalio.client import Client
import asyncio

async def wait_for_temporal():
    for attempt in range(20):
        try:
            client = await Client.connect("temporal:7233")
            print("Connected to Temporal!")
            return client
        except Exception as e:
            print(f"[Attempt {attempt+1}/20] Temporal not ready: {e}")
            await asyncio.sleep(2)
    raise RuntimeError("Could not connect to Temporal.")
