# Kling API

Examples for calling the **Kling API** (Kuaishou text-to-video and image-to-video) through Apiframe.

**Model page:** [Kling API](https://apiframe.ai/models/kling-3.0)

This repo does not host model weights. Kling is a closed model. Inference runs on `POST /v2/videos/generate` with `model: "kling-3.0"`.

Related model ids on the same endpoint: `kling-3.0-omni`, `kling-3.0-motion-control`.

## What is Kling?

Kling 3.0 is Kuaishou's video generation model. It supports text-to-video and image-to-video, 3–15 second clips, optional native audio, and start/end frame control. Modes are `standard` (720p), `pro` (1080p), and `4k`.

## Quick start

```bash
export APIFRAME_API_KEY=afk_your_api_key_here
```

### Python

```bash
pip install requests
```

```python
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
```

### JavaScript

```bash
npm i @apiframe-ai/sdk@next
```

```javascript
import { Apiframe } from "@apiframe-ai/sdk";

const client = new Apiframe({ apiKey: process.env.APIFRAME_API_KEY });

const { jobId } = await client.videos.generate({
  model: "kling-3.0",
  prompt: "a cinematic sunrise over a futuristic cityscape",
  klingParams: {
    duration: 5,
    mode: "pro",
    aspect_ratio: "16:9",
    generate_audio: true,
  },
});

const job = await client.jobs.waitFor(jobId);
console.log(job.result);
```

Pass `webhookUrl` on the generate call if you do not want to poll.

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `prompt` | string | required | Text description of the video |
| `klingParams.duration` | integer | `5` | Seconds: `3`, `5`, `8`, `10`, or `15` |
| `klingParams.mode` | string | `"pro"` | `standard` (720p), `pro` (1080p), `4k` |
| `klingParams.aspect_ratio` | string | `"16:9"` | `1:1`, `9:16`, `16:9` |
| `klingParams.start_image` | string | — | First-frame URL (image-to-video) |
| `klingParams.end_image` | string | — | Last-frame URL |
| `klingParams.generate_audio` | boolean | `false` | Native audio |

Typical latency is about 135 seconds. Output is 1 video (`videoUrl`). Swap `model` for `kling-3.0-omni` (reference images/video) or `kling-3.0-motion-control` (transfer motion from a clip onto a character).

## Image to video

```python
requests.post(
    "https://api.apiframe.ai/v2/videos/generate",
    headers=headers,
    json={
        "model": "kling-3.0",
        "prompt": "slow push in, steam rising from the cup",
        "klingParams": {
            "start_image": "https://example.com/frame.jpg",
            "duration": 5,
            "mode": "pro",
            "aspect_ratio": "16:9",
        },
    },
)
```

## Output

```json
{
  "videoUrl": "https://cdn2.apiframe.ai/videos/….mp4"
}
```

## Examples

| Example | Python | JavaScript |
|---|---|---|
| Text to video | [text_to_video.py](examples/text_to_video.py) | [text_to_video.js](examples/text_to_video.js) |
| Image to video | [image_to_video.py](examples/image_to_video.py) | [image_to_video.js](examples/image_to_video.js) |

```bash
cp .env.example .env
# set APIFRAME_API_KEY
python examples/text_to_video.py
```

## License

Example code in this repository is provided as-is. Kling outputs are subject to Kling's terms. Kling is a trademark of Kuaishou Technology. Apiframe is not affiliated with, endorsed by, or sponsored by Kuaishou Technology.
