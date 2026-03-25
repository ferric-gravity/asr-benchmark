import time
import librosa
import soundfile as sf
from faster_whisper import WhisperModel


class StreamingASR:

    def __init__(self, chunk_duration=2.0):
        self.model = WhisperModel("small", device="cpu")
        self.chunk_duration = chunk_duration

    def transcribe(self, audio_path):

        audio, sr = librosa.load(audio_path, sr=16000)

        chunk_size = int(sr * self.chunk_duration)

        chunks = [
            audio[i:i+chunk_size]
            for i in range(0, len(audio), chunk_size)
        ]

        full_text = ""
        start = time.time()
        first_chunk_time = None

        # for i, chunk in enumerate(chunks):

        #     chunk_path = f"temp_chunk.wav"
        #     sf.write(chunk_path, chunk, sr)

        #     segments, _ = self.model.transcribe(chunk_path)

        #     text = " ".join([seg.text for seg in segments])

        #     if i == 0:
        #         first_chunk_time = time.time() - start

        #     full_text += " " + text
        for i, chunk in enumerate(chunks):
            segments, _ = self.model.transcribe(chunk) 
            text = " ".join([seg.text for seg in segments])
            if i == 0:
                first_chunk_time = time.time() - start
            full_text += " " + text

        total_latency = time.time() - start

        return full_text.strip(), first_chunk_time, total_latency