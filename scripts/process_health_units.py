import sys
import os
import json

# 👇 adiciona a raiz do projeto ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import RAW_DATA_PATH, PROCESSED_DATA_PATH


RAW_FILE = os.path.join(RAW_DATA_PATH, "health_units_teresina.json")
PROCESSED_FILE = os.path.join(
    PROCESSED_DATA_PATH,
    "health_units_teresina.geojson"
)

def load_raw_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def is_valid_coordinate(lat, lon):
    return (
        lat is not None
        and lon is not None
        and -90 <= lat <= 90
        and -180 <= lon <= 180
    )

def build_geojson(health_units):
    features = []

    for unit in health_units:
        lat = unit.get("latitude")
        lon = unit.get("longitude")

        if not is_valid_coordinate(lat, lon):
            continue

        feature = {
            "type": "Feature",
            "properties": {
                "id": unit.get("id"),
                "name": unit.get("name"),
                "type": unit.get("type"),
                "neighborhood": unit.get("neighborhood")
            },
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            }
        }

        features.append(feature)

    return {
        "type": "FeatureCollection",
        "features": features
    }

def save_geojson(geojson_data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(geojson_data, f, ensure_ascii=False, indent=2)

def main():
    raw_data = load_raw_data(RAW_FILE)
    health_units = raw_data.get("health_units", [])

    geojson = build_geojson(health_units)
    save_geojson(geojson, PROCESSED_FILE)

    print(f"✔ GeoJSON gerado com {len(geojson['features'])} unidades.")

if __name__ == "__main__":
    main()
