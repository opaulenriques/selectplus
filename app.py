
import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Select+", layout="wide")

# Simulação de dados de vagas
dados = pd.DataFrame([
    {"vaga": "Analista RH", "status": "Em andamento", "marca": "O Boticário", "recrutador": "Ana"},
    {"vaga": "Vendedor", "status": "Finalizada", "marca": "Eudora", "recrutador": "Carlos"},
    {"vaga": "Financeiro", "status": "Cancelada", "marca": "Levi's", "recrutador": "Ana"},
    {"vaga": "Estágio", "status": "Congelada", "marca": "Hering", "recrutador": "João"},
])

st.title("📋 Sistema Select+")
st.markdown("**Exportar relatórios de vagas**")

filtro_status = st.selectbox("Filtrar por status da vaga", options=["Todas", "Em andamento", "Finalizada", "Cancelada", "Congelada"])
filtro_recrutador = st.selectbox("Filtrar por recrutador", options=["Todos"] + list(dados["recrutador"].unique()))

df_filtrado = dados.copy()
if filtro_status != "Todas":
    df_filtrado = df_filtrado[df_filtrado["status"] == filtro_status]
if filtro_recrutador != "Todos":
    df_filtrado = df_filtrado[df_filtrado["recrutador"] == filtro_recrutador]

st.dataframe(df_filtrado, use_container_width=True)

def gerar_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Vagas")
    processed_data = output.getvalue()
    return processed_data

excel_data = gerar_excel(df_filtrado)
st.download_button(label="📥 Baixar Excel", data=excel_data, file_name="relatorio_vagas.xlsx", mime="application/vnd.ms-excel")
