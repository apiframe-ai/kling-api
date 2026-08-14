import os
import time
import requests

API = "https://api.apiframe.ai/v2"
headers = {
    "X-API-Key": os.environ["APIFRAME_API_KEY"],
    "Content-Type": "application/json",
}

start_image = os.environ.get("START_IMAGE", "https://example.com/frame.jpg")

job = requests.post(
    f"{API}/videos/generate",
    headers=headers,
    json={
        "model": "kling-3.0",
        "prompt": "slow push in, steam rising from the cup",
        "klingParams": {
            "start_image": start_image,
            "duration": 5,
            "mode": "pro",
            "aspect_ratio": "16:9",
        },
    },
).json()

while True:
    result = requests.get(f"{API}/jobs/{job['jobId']}", headers=headers).json()
    if result["status"] in ("COMPLETED", "FAILED"):
        break
    time.sleep(2)

print(result.get("result"))
