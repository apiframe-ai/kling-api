import os
import time
import requests

API = "https://api.apiframe.ai/v2"
headers = {
    "X-API-Key": os.environ["APIFRAME_API_KEY"],
    "Content-Type": "application/json",
}

job = requests.post(
    f"{API}/videos/generate",
    headers=headers,
    json={
        "model": "kling-3.0",
        "prompt": "a cinematic sunrise over a futuristic cityscape",
        "klingParams": {
            "duration": 5,
            "mode": "pro",
            "aspect_ratio": "16:9",
            "generate_audio": True,
        },
    },
).json()

while True:
    result = requests.get(f"{API}/jobs/{job['jobId']}", headers=headers).json()
    if result["status"] in ("COMPLETED", "FAILED"):
        break
    time.sleep(2)

print(result.get("result"))
