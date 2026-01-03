import streamlit as st
import pydeck as pdk
from services.brasilio import load_health_units_teresina
from services.ibge import get_teresina_population
from map.layers import health_units_layer

st.set_page_config(layout="wide")

st.title("Mapa Inteligente de Serviços Públicos — Teresina / PI")

population = get_teresina_population()
st.markdown(
    f"""
    **Município:** {population['municipio']} - {population['uf']}  
    **População estimada:** {population['populacao_estimada']:,}
    """
)

df_health = load_health_units_teresina()

st.write(f"Unidades de saúde encontradas: {len(df_health)}")

layer = health_units_layer(df_health)

view_state = pdk.ViewState(
    latitude=-5.0892,
    longitude=-42.8019,
    zoom=12
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{nome_fantasia}"}
)

st.pydeck_chart(deck)
