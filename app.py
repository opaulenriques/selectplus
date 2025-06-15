import streamlit as st
from vaga_utils import criar_vaga, listar_vagas
from vaga_model import Base
from database import engine
from datetime import date

# Cria as tabelas
Base.metadata.create_all(bind=engine)

st.set_page_config(page_title="Sistema de R&S", layout="wide")
st.title("Sistema de Recrutamento e Seleção")

menu = st.sidebar.selectbox("Menu", ["Cadastrar Vaga", "Visualizar Vagas"])

if menu == "Cadastrar Vaga":
    st.subheader("Cadastrar nova vaga")
    with st.form("form_vaga"):
        data_abertura = st.date_input("Data de Abertura", value=date.today())
        sla = st.number_input("SLA (dias)", min_value=1)
        marca = st.selectbox("Marca", ["O Boticário", "Quem Disse, Berenice?", "Eudora", "Hering", "Levi's", "Escritório"])
        departamento = st.text_input("Departamento")
        solicitante = st.text_input("Solicitante")
        cargo = st.text_input("Cargo")
        sigilosa = st.checkbox("Vaga Sigilosa?")
        tipo_vaga = st.selectbox("Tipo de Vaga", ["Operacional", "Estratégica"])
        recrutador = st.text_input("Recrutador Responsável")
        status = st.selectbox("Status da Vaga", ["Aberta", "Fechada", "Congelada", "Cancelada"])
        etapa = st.text_input("Etapa Atual")
        fonte = st.text_input("Fonte da Vaga")
        observacoes = st.text_area("Histórico / Observações")

        submitted = st.form_submit_button("Salvar")
        if submitted:
            dados = {
                "data_abertura": data_abertura,
                "sla": sla,
                "marca": marca,
                "departamento": departamento,
                "solicitante": solicitante,
                "cargo": cargo,
                "sigilosa": sigilosa,
                "tipo_vaga": tipo_vaga,
                "recrutador": recrutador,
                "status": status,
                "etapa": etapa,
                "fonte": fonte,
                "observacoes": observacoes
            }
            criar_vaga(dados)
            st.success("Vaga cadastrada com sucesso!")

elif menu == "Visualizar Vagas":
    st.subheader("Lista de Vagas")
    vagas = listar_vagas()
    for vaga in vagas:
        st.markdown(f"""
        **ID:** {vaga.id}  
        **Cargo:** {vaga.cargo}  
        **Marca:** {vaga.marca}  
        **Status:** {vaga.status}  
        **Recrutador:** {vaga.recrutador}  
        **Observações:** {vaga.observacoes}  
        ---
        """)
