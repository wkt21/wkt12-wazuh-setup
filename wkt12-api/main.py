from fastapi import FastAPI, Request
from models import WazuhAlert
import yaml
from pathlib import Path

app = FastAPI(title="WKT12 Intel Center API", version="1.0.0")

# Load config
config_path = Path(__file__).parent / "config.yaml"
with open(config_path) as f:
    config = yaml.safe_load(f)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/intel/wazuh")
async def ingest_wazuh(request: Request):
    payload = await request.json()
    alert = WazuhAlert(**payload)

    killfeed_event = {
        "type": "wazuh_alert",
        "severity": alert.severity,
        "summary": alert.summary,
        "host": alert.host,
        "rule_id": alert.rule_id,
        "raw": payload
    }

    # TODO: send to your Intel Center (HTTP, message bus, etc.)
    # Example:
    # import httpx
    # async with httpx.AsyncClient() as client:
    #     await client.post(
    #         f"{config['intel_center']['base_url']}{config['intel_center']['killfeed_endpoint']}",
    #         json=killfeed_event,
    #         headers={"Authorization": f"Bearer {config['intel_center']['api_key']}"}
    #     )

    print(f"[WKT12] Received alert: rule={alert.rule_id} severity={alert.severity} host={alert.host}")
    return {"status": "ok", "received": alert.rule_id}
