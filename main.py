
from fastapi import FastAPI
from generators import siem, edr, ndr, cloud, threatFeed, cve
from algoliaClient import push_to_algolia
import asyncio

app = FastAPI()

@app.get("/generate")
async def generate():
    data = []
    data.extend([siem.generate_siem_event() for _ in range(5)])
    # Repeat for other sources...
    data.extend([edr.generate_edr_event() for _ in range(5)])
    data.extend([ndr.generate_ndr_event() for _ in range(5)])
    data.extend([cloud.generate_cloud_event() for _ in range(5)])
    data.extend([threatFeed.generate_threat_feed_event() for _ in range(5)])
    data.extend([cve.generate_cve_event() for _ in range(5)])
    await push_to_algolia(data)
    return {"status": "pushed", "count": len(data)}
@app.get("/")
async def root():
    return {"message": "Welcome to the Cyber Synthetic Data API. Use /generate to create synthetic data."}
@app.get("/health")
async def health():
    return {"status": "healthy"}
@app.get("/status")
async def status():
    return {"status": "running"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# To run this FastAPI application, use the command:
# uvicorn main:app --reload
# Ensure you have the required libraries installed:
# pip install fastapi uvicorn algoliasearch
# and the generators and algolia_client modules are properly set up in your project structure.
# This code sets up a FastAPI application that generates synthetic cybersecurity data from various sources
# and pushes it to Algolia for indexing. The `/generate` endpoint creates synthetic events from multiple sources,
# pushes them to Algolia, and returns the count of generated events. The root endpoint provides a welcome message,
# and the `/health` and `/status` endpoints provide basic health checks for the application.