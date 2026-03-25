import time
from faster_whisper import WhisperModel

class OfflineASR:

    def __init__(self):
        self.model = WhisperModel("small", device="cpu")

    def transcribe(self, audio_path):

        start = time.time()

        segments, _ = self.model.transcribe(audio_path)

        text = " ".join([seg.text for seg in segments]).strip()

        latency = time.time() - start

        return text, latency