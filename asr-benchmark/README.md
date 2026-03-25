# ASR Benchmark: Streaming vs Offline Transcription

This project benchmarks offline and streaming Automatic Speech Recognition (ASR) using Faster Whisper on Hindi/Hinglish audio. It evaluates latency and accuracy tradeoffs relevant to real-time voice systems.

---

## Overview

The goal is to compare:

- Offline transcription (full audio input)
- Streaming transcription (chunk-based simulation)

Metrics evaluated:

- Latency (p50 / p95)
- First-token latency (streaming only)
- Word Error Rate (WER)

---

## Setup

**Model**
- Faster Whisper (small)

**Hardware**
- Apple M2 CPU (no GPU acceleration)

**Dataset**
- 20 Hindi/Hinglish audio samples
- Duration: 5–20 seconds per clip
- Conversational and semi-structured speech

---

## Project Structure
asr-benchmark/

data/
metadata_sample.csv

src/
data_loader.py
offline_asr.py
streaming_asr.py
metrics.py
benchmark.py

requirements.txt
README.md

---

## Installation

Create a clean environment (recommended):
conda create -n asr_env python=3.10 -y
conda activate asr_env
Install dependencies: pip install -r requirements.txt
---

## Running the Benchmark
python src/benchmark.py

---

## Results

### Offline Transcription

- p50 latency: ~3.03s  
- p95 latency: ~5.26s  
- WER: ~0.56  

---

### Streaming Transcription (2s chunks)

- p50 latency: ~7.20s  
- p95 latency: ~81.29s  
- First-token latency (p50): ~2.63s  
- WER: ~0.79  

---

## Key Observations

- Offline transcription provides lower overall latency and better accuracy.
- Streaming reduces time to first response but increases total latency.
- WER is higher in streaming mode due to limited context per chunk.

---

## Key Insight

Naive chunk-based streaming increases total latency because the model is re-run independently for each chunk without reusing intermediate computation (e.g., KV cache).

This highlights a key tradeoff in ASR systems:

- Lower latency (streaming) improves responsiveness  
- Higher context (offline) improves accuracy  

---

## Limitations

- Streaming is simulated using chunked inference, not true incremental decoding
- No reuse of model state across chunks
- CPU-only setup limits performance

---

## Future Work

- Implement stateful decoding or KV cache reuse
- Benchmark native streaming models (e.g., Voxtral Realtime)
- Evaluate different chunk sizes (1s, 2s, 4s)
- Test under concurrent load
- Compare quantized models for latency improvements

---

## Notes

This project was built to explore real-world tradeoffs in ASR systems for latency-sensitive applications such as voice-based customer support and banking workflows.
