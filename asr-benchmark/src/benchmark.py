from data_loader import load_dataset
from offline_asr import OfflineASR
from streaming_asr import StreamingASR
from metrics import compute_wer, compute_stats


dataset = load_dataset("data/metadata.csv", "data/audio/train")

offline_model = OfflineASR()
streaming_model = StreamingASR()

offline_latencies = []
streaming_latencies = []
streaming_first_token = []

offline_wers = []
streaming_wers = []

for audio_path, reference in dataset[:20]:

    # OFFLINE
    pred_offline, lat_offline = offline_model.transcribe(audio_path)

    offline_latencies.append(lat_offline)
    offline_wers.append(compute_wer(reference, pred_offline))

    # STREAMING
    pred_stream, first_lat, total_lat = streaming_model.transcribe(audio_path)

    streaming_latencies.append(total_lat)
    streaming_first_token.append(first_lat)
    streaming_wers.append(compute_wer(reference, pred_stream))


print("\nOFFLINE")
print("Latency:", compute_stats(offline_latencies))
print("WER:", sum(offline_wers)/len(offline_wers))

print("\nSTREAMING")
print("Latency:", compute_stats(streaming_latencies))
print("First Token Latency:", compute_stats(streaming_first_token))
print("WER:", sum(streaming_wers)/len(streaming_wers))