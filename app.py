# ---------------------------------------------------------------------------
# DASHBOARD INTERATIVO - PREVISÃO DE CUSTOS DE SEGURO
# Descrição: Um aplicativo web simples para prever os custos de seguro
#            usando o modelo treinado.
# Autor: Seu Nome
# Ferramenta: Streamlit
# ---------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuração da Página ---
st.set_page_config(
    page_title="Previsão de Custos de Seguro",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)


# --- Funções Auxiliares ---

# Usar cache para carregar o modelo apenas uma vez
@st.cache_data
def load_model(path):
    """Carrega o modelo a partir do caminho especificado."""
    if os.path.exists(path):
        modelo = joblib.load(path)
        return modelo
    else:
        st.error(f"Modelo não encontrado em '{path}'. Por favor, treine o modelo primeiro.")
        return None

@st.cache_data
def load_data(path):
    """Carrega o dataset para visualizações."""
    if os.path.exists(path):
        df = pd.read_csv(path)
        return df
    else:
        st.error(f"Dataset não encontrado em '{path}'.")
        return None


# --- Carregamento de Dados e Modelo ---
model_path = os.path.join('models', 'random_forest_regressor.pkl')
data_path = os.path.join('data', 'insurance.csv')

modelo_carregado = load_model(model_path)
df = load_data(data_path)


# --- Interface do Usuário (Sidebar) ---
st.sidebar.title("Calculadora de Custo de Seguro")
st.sidebar.markdown("Insira as informações do cliente para prever o custo anual do seguro.")

# Inputs do usuário
age = st.sidebar.slider("Idade", 18, 100, 35)
bmi = st.sidebar.slider("Índice de Massa Corporal (IMC)", 15.0, 55.0, 26.5, 0.1)
children = st.sidebar.selectbox("Número de Filhos", [0, 1, 2, 3, 4, 5])
smoker = st.sidebar.radio("É Fumante?", ("Não", "Sim"))
sex = st.sidebar.radio("Sexo", ("Masculino", "Feminino"))
region = st.sidebar.selectbox("Região", ("Noroeste", "Nordeste", "Sudoeste", "Sudeste"))


# --- Preparação dos Dados para Previsão ---
# Mapear os inputs para os valores que o modelo espera
sex_map = {"Masculino": "male", "Feminino": "female"}
smoker_map = {"Sim": "yes", "Não": "no"}
region_map = {
    "Noroeste": "northwest",
    "Nordeste": "northeast",
    "Sudoeste": "southwest",
    "Sudeste": "southeast"
}

# Criar um DataFrame com os dados do usuário
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex_map[sex]],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker_map[smoker]],
    'region': [region_map[region]]
})


# --- Previsão e Exibição do Resultado ---
st.title("🏥 Previsão de Custos de Seguro Médico")
st.markdown("Este dashboard utiliza um modelo de Machine Learning para estimar os encargos médicos de um indivíduo com base em suas características.")

if modelo_carregado is not None:
    prediction = modelo_carregado.predict(input_data)[0]

    st.subheader("Resultado da Previsão")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Custo Anual Previsto",
            value=f"R$ {prediction:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            help="Este é o valor estimado pelo modelo Random Forest."
        )

    with col2:
        if smoker == "Sim":
            st.warning("O fato de ser fumante aumenta significativamente o custo do seguro.")
        else:
            st.success("Não ser fumante é um fator chave para manter os custos baixos.")


# --- Visualizações Claras (Etapa 5) ---
st.markdown("---")
st.header("Visualizações e Insights do Modelo")
st.markdown("Analisando os dados que treinaram o modelo, podemos extrair os seguintes insights:")

if df is not None:
    col1_viz, col2_viz = st.columns(2)

    with col1_viz:
        st.subheader("Custos: Fumantes vs. Não Fumantes")
        fig, ax = plt.subplots()
        sns.boxplot(x='smoker', y='charges', data=df, ax=ax, palette='viridis')
        ax.set_title("Impacto do Fumo nos Custos")
        ax.set_xlabel("Fumante")
        ax.set_ylabel("Custos (R$)")
        st.pyplot(fig)
        st.markdown("Como o gráfico mostra, ser fumante é o fator de maior impacto individual no custo do seguro.")

    with col2_viz:
        st.subheader("Correlação: Idade vs. Custos")
        fig, ax = plt.subplots()
        sns.scatterplot(x='age', y='charges', data=df, hue='smoker', ax=ax, alpha=0.6)
        ax.set_title("Relação entre Idade e Custos")
        ax.set_xlabel("Idade")
        ax.set_ylabel("Custos (R$)")
        st.pyplot(fig)
        st.markdown("Há uma tendência clara de aumento dos custos com a idade, e essa tendência é muito mais acentuada para fumantes.")
