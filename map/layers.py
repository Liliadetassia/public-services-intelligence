import pydeck as pdk

def health_units_layer(df):
    return pdk.Layer(
        "ScatterplotLayer",
        df,
        get_position='[longitude, latitude]',
        get_radius=120,
        get_fill_color=[255, 140, 0],
        pickable=True,
    )
