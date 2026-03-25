from jiwer import wer
import numpy as np

def compute_wer(reference, prediction):
    return wer(reference, prediction)

def compute_stats(latencies):

    return {
        "avg": np.mean(latencies),
        "p50": np.percentile(latencies, 50),
        "p95": np.percentile(latencies, 95)
    }