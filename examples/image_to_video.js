import { Apiframe } from "@apiframe-ai/sdk";

const client = new Apiframe({ apiKey: process.env.APIFRAME_API_KEY });
const startImage = process.env.START_IMAGE || "https://example.com/frame.jpg";

const { jobId } = await client.videos.generate({
  model: "kling-3.0",
  prompt: "slow push in, steam rising from the cup",
  klingParams: {
    start_image: startImage,
    duration: 5,
    mode: "pro",
    aspect_ratio: "16:9",
  },
});

const job = await client.jobs.waitFor(jobId);
console.log(job.result);
