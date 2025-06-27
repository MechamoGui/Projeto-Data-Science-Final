# Análise Preditiva de Custos de Seguro de Saúde 🏥
Este repositório contém um projeto completo de Data Science, desde a análise exploratória de dados até a criação de um modelo preditivo para prever os custos de seguros de saúde.

Autor: Guilherme Victor de Melo Gonçalves

Data: 27/06/2025

    Assista ao Vídeo Explicativo do Projeto: > (`https://www.youtube.com/watch?v=ADULo8KYSKU `)


## 🎯 1. Descrição do Problema
Uma companhia de seguros precisa de uma maneira mais precisa e automatizada para calcular os prêmios (custos) de seguro de saúde. O objetivo deste projeto é desenvolver um modelo de Machine Learning capaz de estimar os custos médicos anuais de um indivíduo com base em suas características demográficas e de saúde. Uma previsão precisa permite à empresa otimizar a precificação, tornando-a mais justa para o cliente e financeiramente sustentável para o negócio.

## 🗂️ 2. Estrutura do Projeto
    Assista ao Vídeo Explicativo do Projeto:        
    📂 data/
    │  
    └── 📄 insurance.csv
    
    📂 img/
    │  
    └── 🖼️ (Gráficos gerados pela análise)
   
    
    📂 models
    │  
    └──📦 random_forest_regressor.pkl
    
    📂 notebooks/
    │  
    └──📓 analise_de_seguro.ipynb
    
    ── 📜 requirements.txt
    
    ── 📄 README.md


## 🚀 3. Guia de Utilização do ProjetoSiga os passos abaixo para configurar e executar este projeto em sua máquina local.
### Pré-requisitos: 

- Python (`https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe`)
- Git

### 1: Clone o Repositório 
Abra seu terminal e clone este repositório para sua máquina local:
```sh
git clone < https://github.com/MechamoGui/Projeto-Data-Science-Final.git >
 ```
 ```sh
cd < NOME_DA_PASTA_DO_PROJETO >
 ```
### 2: Configure o Ambiente Virtual
É uma boa prática criar um ambiente virtual para isolar as dependências.
Criar o ambiente virtual (venv)
```sh
python -m venv venv
```
### Ativar o ambiente virtual

#### No Windows:
 ```sh
.\venv\Scripts\activate
```
#### No macOS/Linux:
 ```sh
source venv/bin/activate
```
### 3: Instale as Dependências
Com o ambiente virtual ativo, instale todas as bibliotecas necessárias:
```sh
pip install -r requirements.txt
```

### 4: Execute a Análise 
Para ver todo o processo de análise, limpeza, treinamento e avaliação do modelo:
Inicie o 
- Jupyter Lab

## 🛠️ 4. Técnicas e Ferramentas Utilizadas
- Limpeza e Preparação: Remoção de duplicatas, codificação com One-Hot Encoding e padronização com StandardScaler.

- Análise Exploratória (EDA): Geração de histogramas, boxplots e matriz de correlação com Matplotlib e Seaborn.

- Modelagem Preditiva: Treinamento e avaliação de modelos de Scikit-learn (Regressão Linear e Random Forest Regressor).

- Ambiente de Desenvolvimento: Análise realizada em Jupyter Notebook.

- Versionamento: Controle de versão realizado com `Git` e `GitHub`.
  
## 📊 5. Resultados e Métricas dos Modelos
Os modelos foram avaliados utilizando R² (Coeficiente de Determinação) e RMSE (Raiz do Erro Quadrático Médio).

    ModeloR²                  (R-squared)              RMSE (Erro Médio)

    Regressão Linear          0.7833                   $5.796,28

    Random Forest Regressor   0.8655                   $4.547,41

O Random Forest foi o modelo escolhido devido ao seu desempenho superior, sendo salvo em `models/random_forest_regressor.pkl.`

## 🖥️​ 6: Executar o Dashboard Interativo

Ative o Ambiente Virtual:
```sh
.\venv\Scripts\activate
```
Instale o Streamlit:
- Com o ambiente virtual (venv) ativo, instale a biblioteca:
```sh
pip install streamlit
```
Inicie o Dashboard:
- No terminal, na pasta raiz do projeto, execute o comando:
```sh
streamlit run app.py
```
- Uma nova aba será aberta em seu navegador com o dashboard interativo.
  
## 💡 7. Conclusão e Sugestões
A análise e a modelagem permitiram concluir que:

- Impacto do Tabagismo: Ser fumante é o fator de maior impacto individual no custo do seguro.

- Idade e IMC: São fatores importantes com correlação positiva clara com os custos.

- Eficácia do Modelo: O modelo Random Forest é uma ferramenta eficaz para a tarefa, servindo como uma base sólida para otimizar a precificação de apólices.

