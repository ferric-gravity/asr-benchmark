import csv
import os

def clean_text(text):
    text = text.lower()
    text = text.replace(",", "").replace(".", "")
    return text.strip()

def load_dataset(csv_path, audio_base_path):
    dataset = []

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            audio_path = os.path.join(audio_base_path, row["audio"].split("/")[-1])
            text = clean_text(row["text"])

            dataset.append((audio_path, text))

    return dataset