import json
from pathlib import Path

def check_required_labels(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    if data['sarung_tangan'] >= 2 and data['jas_laboratorium'] >= 1 and data['kacamata_pelindung'] >= 1:
        return True
    return False

# Contoh penggunaan
json_file = 'D:\Code\SAFE\MQTT-YOLOV5\detectedIMG\IMG-20240721-WA0018_labels.json'  # Ubah path sesuai dengan lokasi JSON Anda
result = check_required_labels(json_file)
print(f"All required labels present: {result}")