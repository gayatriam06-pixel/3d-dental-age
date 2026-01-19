import re
import pandas as pd
from pathlib import Path
from feature_extraction import extract_features
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR

PATTERN = r".+_([MF])(\d+)_.*\.stl"

def parse_labels(filename):
    match = re.match(PATTERN, filename)
    if not match:
        return None, None

    sex = 1 if match.group(1) == "M" else 0
    age = int(match.group(2))
    return age, sex

def build_dataset():
    rows = []

    for stl_file in RAW_DATA_DIR.glob("*.stl"):
        age, sex = parse_labels(stl_file.name)
        if age is None:
            continue

        features = extract_features(stl_file)

        rows.append({
            "volume": features[0],
            "surface_area": features[1],
            "bbox_mean": features[2],
            "face_count": features[3],
            "vertex_count": features[4],
            "age": age,
            "sex": sex
        })

    df = pd.DataFrame(rows)
    output_path = PROCESSED_DATA_DIR / "dataset.csv"
    df.to_csv(output_path, index=False)

    print(f"Dataset saved to {output_path}")

if __name__ == "__main__":
    build_dataset()
