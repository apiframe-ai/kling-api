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
