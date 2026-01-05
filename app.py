import json
import streamlit as st
import pydeck as pdk
from config import (
    CITY_NAME,
    CITY_LATITUDE,
    CITY_LONGITUDE,
    MAP_ZOOM,
    PROCESSED_DATA_PATH
)

# -------------------------------
# Configuração da página
# -------------------------------
st.set_page_config(
    page_title="Mapa de Unidades de Saúde – Teresina",
    layout="wide"
)

st.title("🏥 Unidades de Saúde Públicas – Teresina / PI")
st.markdown(
    """
    Visualização interativa de unidades de saúde públicas
    utilizando dados abertos e georreferenciamento.
    """
)

# -------------------------------
# Carregar GeoJSON
# -------------------------------
GEOJSON_FILE = f"{PROCESSED_DATA_PATH}/health_units_teresina.geojson"

with open(GEOJSON_FILE, "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

features = geojson_data["features"]

# -------------------------------
# Filtro por tipo
# -------------------------------
types_available = sorted(
    list(set(f["properties"]["type"] for f in features))
)

selected_types = st.multiselect(
    "Filtrar por tipo de unidade:",
    options=types_available,
    default=types_available
)

filtered_features = [
    f for f in features
    if f["properties"]["type"] in selected_types
]

filtered_geojson = {
    "type": "FeatureCollection",
    "features": filtered_features
}

st.write(f"🔎 {len(filtered_features)} unidades exibidas")

# -------------------------------
# Camada Deck.GL
# -------------------------------
layer = pdk.Layer(
    "GeoJsonLayer",
    data=filtered_geojson,
    pickable=True,
    auto_highlight=True,
    filled=True,
    extruded=False,
    get_fill_color=[255, 140, 0, 180],  # laranja institucional
    get_radius=80
)

view_state = pdk.ViewState(
    latitude=CITY_LATITUDE,
    longitude=CITY_LONGITUDE,
    zoom=MAP_ZOOM
)

tooltip = {
    "html": "<b>{name}</b><br/>Tipo: {type}<br/>Bairro: {neighborhood}",
    "style": {"backgroundColor": "black", "color": "white"}
}

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip,
    map_style=None  # sem Mapbox
)

st.pydeck_chart(deck)
