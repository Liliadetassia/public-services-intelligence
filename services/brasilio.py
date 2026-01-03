import requests
import pandas as pd

BASE_URL = "https://api.brasil.io/v1/dataset/cnes/estabelecimentos/data/"

def load_health_units_teresina(max_records=500):
    results = []
    page = 1
    page_size = 100

    while len(results) < max_records:
        params = {
            "page": page,
            "page_size": page_size
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()
        results.extend(data["results"])

        if not data["next"]:
            break

        page += 1

    df = pd.DataFrame(results)

    # Filtrar especificamente Teresina / PI
    df = df[
        (df["municipio"] == "TERESINA") &
        (df["uf"] == "PI")
    ]

    return df.head(max_records)
