import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
medalhistas = pd.read_csv(r'medalists.csv')
paises = pd.read_csv(r'countries.csv')
delegacoes = pd.read_csv(r'delegations.csv')
medalhas = pd.read_csv(r'medals.csv')
esportes = pd.read_csv(r'sports.csv')

# Mesclar os dados para contar medalhas por país
medalhas_por_pais = pd.merge(medalhistas, paises, on='country_id')
medalhas_por_pais = medalhas_por_pais['country_name'].value_counts().reset_index()
medalhas_por_pais.columns = ['País', 'Medalhas']

# Criar um seletor para escolher o número de países a serem exibidos
num_paises = st.slider('Escolha o número de países a serem exibidos:', min_value=1, max_value=len(medalhas_por_pais), value=5)

# Ordenar e selecionar os países com mais medalhas
medalhas_selecionadas = medalhas_por_pais.nlargest(num_paises, 'Medalhas')

# Criar o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
medalhas_selecionadas.plot(kind='barh', x='País', y='Medalhas', color='skyblue', ax=ax)
ax.set_title('Distribuição de Medalhas por País')
ax.set_xlabel('Número de Medalhas')
ax.set_ylabel('País')

# Exibir o gráfico no Streamlit
st.pyplot(fig)
