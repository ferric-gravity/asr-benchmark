# ASR Serving Benchmark — Streaming vs Offline (Whisper)

## Setup

Model:
Faster Whisper (small)

Hardware:
Apple M2 (CPU)

Dataset:
20 Hindi / Hinglish audio clips (5–20 seconds each)

---

## Experiment

Compared:

1. Offline transcription (full audio)
2. Streaming transcription (chunk-based simulation)

Measured:
- Total latency (p50 / p95)
- First-token latency
- WER (Word Error Rate)

---

## Results

### Offline

- p50 latency: 3.03s
- p95 latency: 5.26s
- WER: 0.56

---

### Streaming (2s chunks)

- p50 latency: 7.20s
- p95 latency: 81.29s
- First-token latency (p50): 2.63s
- WER: 0.79

---

## Observations

- Streaming implementation showed significantly higher total latency than offline inference.
- This is due to repeated full-model inference for each chunk, without reusing intermediate states (e.g., KV cache).
- First-token latency is lower than full offline latency, improving responsiveness.

---

## Key Insight

Naive chunk-based streaming increases total latency due to repeated computation, even though it improves responsiveness.

This highlights a fundamental tradeoff in ASR systems:

- Lower latency (streaming) → worse WER, higher compute
- Higher accuracy (offline) → better WER, slower response

---

## Limitations

- Streaming is simulated (not true incremental decoding)
- No state reuse between chunks
- CPU-only setup

---

## What I Would Try Next

- Use stateful decoding / KV cache reuse
- Benchmark Voxtral Realtime (native streaming model)
- Compare chunk sizes (1s vs 2s vs 4s)
- Evaluate performance under concurrent requests
- Test quantized models for latency improvements

---

## Notes

This experiment was conducted as part of exploring real-time ASR tradeoffs for voice AI systems (e.g., banking pipelines).