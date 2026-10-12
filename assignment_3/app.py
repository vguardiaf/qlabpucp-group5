"""Dashboard de lluvias y emergencias por departamento.

Correr en local (desde assignment_3/):
    streamlit run app.py
"""

import json
import unicodedata
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

CARPETA = Path(__file__).parent / "datos"

# ---------------------------------------------------------------- configuracion
st.set_page_config(page_title="Lluvias en el Perú", page_icon="🌧️", layout="wide")


def normalizar(texto):
    """'Áncash' -> 'ANCASH', para unir la tabla con el geojson."""
    sin_tildes = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return sin_tildes.upper()


# ------------------------------------------------------------------ carga datos
# @st.cache_data guarda el resultado: sin esto, el archivo se lee otra vez
# cada vez que alguien mueve un filtro y la app va lentísima.
@st.cache_data
def cargar():
    datos = pd.read_csv(CARPETA / "tabla-final.csv", dtype={"ubigeo": str},
                        encoding="utf-8-sig")
    # El geojson trae los nombres en mayúsculas y sin tildes
    datos["clave"] = datos["departamento"].map(normalizar)

    with open(CARPETA / "departamentos_peru.geojson", encoding="utf-8") as f:
        formas = json.load(f)
    return datos, formas


datos, formas = cargar()

# ----------------------------------------------------------------------- filtros
st.sidebar.header("Filtros")

departamentos = sorted(datos["departamento"].unique())

elegidos = st.sidebar.multiselect(
    "Departamento", departamentos, default=departamentos
)

minimo = st.sidebar.slider(
    "Lluvia total mínima (mm)", 0, int(datos["lluvia_total_mm"].max()), 0, step=50
)
variables = {
    "Lluvia total (mm)": "lluvia_total_mm",
    "Días de lluvia fuerte": "dias_lluvia_fuerte",
}
variable_mapa = st.sidebar.selectbox("Variable del mapa", list(variables))
columna_mapa = variables[variable_mapa]

filtrado = datos[
    datos["departamento"].isin(elegidos) & (datos["lluvia_total_mm"] >= minimo)
]

# ------------------------------------------------------------------------ titulo
st.title("🌧️ Lluvia total y lluvias fuertes por departamento")
st.caption("Lluvia medida en la estación de la capital de cada departamento")

if filtrado.empty:
    st.warning("No hay departamentos que cumplan los filtros. Ajusta la selección.")
    st.stop()

# ---------------------------------------------------------------------- metricas
c1, c2, c3, c4 = st.columns(4)
c1.metric("Departamentos", f"{len(filtrado):,}")
c2.metric("Lluvia promedio (mm)", f"{filtrado['lluvia_total_mm'].mean():,.1f}")
c3.metric("Días de lluvia fuerte", f"{int(filtrado['dias_lluvia_fuerte'].sum()):,}")
c4.metric("Declaratorias de emergencia", f"{int(filtrado['declaratorias'].sum()):,}")

st.divider()

# ---------------------------------------------------------------------- graficos
izq, der = st.columns(2)

with izq:
    st.subheader("Lluvia total por departamento")
    fig = px.bar(
        filtrado.sort_values("lluvia_total_mm"),
        x="lluvia_total_mm", y="departamento", orientation="h",
        color="lluvia_total_mm", color_continuous_scale="Blues",
        labels={"lluvia_total_mm": "Lluvia total (mm)", "departamento": ""},
    )
    fig.update_layout(coloraxis_showscale=False, template="plotly_white", height=500)
    st.plotly_chart(fig, width="stretch")

with der:
    st.subheader("Lluvia total vs. días de lluvia fuerte")
    fig = px.scatter(
        filtrado,
        x="lluvia_total_mm", y="dias_lluvia_fuerte",
        hover_name="departamento", hover_data={"capital": True},
        labels={"lluvia_total_mm": "Lluvia total (mm)",
                "dias_lluvia_fuerte": "Días de lluvia fuerte",
                "capital": "Capital"},
    )
    fig.update_traces(marker_size=10)
    fig.update_layout(template="plotly_white", height=500)
    st.plotly_chart(fig, width="stretch")

# -------------------------------------------------------------------------- mapa
st.subheader(f"Mapa departamental: {variable_mapa}")

fig = px.choropleth_map(
    filtrado,
    geojson=formas,
    locations="clave",
    featureidkey="properties.departamento",
    color=columna_mapa,
    color_continuous_scale="Blues",
    map_style="carto-positron",
    zoom=4.5,
    center={"lat": -9.2, "lon": -75.0},
    opacity=0.7,
    hover_name="departamento",
    hover_data={"clave": False, "capital": True,
                "lluvia_total_mm": True, "dias_lluvia_fuerte": True},
    labels={"lluvia_total_mm": "Lluvia total (mm)",
            "dias_lluvia_fuerte": "Días de lluvia fuerte",
            "capital": "Capital"},
    height=550,
)
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
st.plotly_chart(fig, width="stretch")

# ------------------------------------------------------------------------- tabla
st.subheader("Departamentos con más días de lluvia fuerte")

tabla = filtrado.drop(columns=["clave"])

st.dataframe(
    tabla.sort_values("dias_lluvia_fuerte", ascending=False)[
        ["departamento", "capital", "lluvia_total_mm",
         "dias_lluvia_fuerte", "declaratorias"]
    ],
    width="stretch",
    hide_index=True,
)

st.download_button(
    "Descargar datos filtrados (CSV)",
    tabla.to_csv(index=False).encode("utf-8"),
    "lluvias_filtrado.csv",
    "text/csv",
)