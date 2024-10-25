import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

medalhistas = pd.read_csv(r'medalists.csv')
paises = pd.read_csv(r'countries.csv')
delegacoes = pd.read_csv(r'delegations.csv')
medalhas = pd.read_csv(r'medals.csv')
esportes = pd.read_csv(r'sports.csv')


df = pd.merge(medalhistas, paises, on='country_id')[['medal', 'country_name']]
df.columns = ['Medalha', 'País']

# Criar um seletor para escolher o número de países a serem exibidos
num_paises = st.selectbox('Escolha o número de países a serem exibidos:', options=range(1, len(medalhas_por_pais) + 1))

# Ordenar e selecionar os países com mais medalhas
medalhas_selecionadas = medalhas_por_pais.nlargest(num_paises, 'Medalhas')

# Criar o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
medalhas_selecionadas.plot(kind='barh', color='skyblue', ax=ax)
ax.set_title('Distribuição de Medalhas por País')
ax.set_xlabel('Número de Medalhas')
ax.set_ylabel('País')

# Exibir o gráfico no Streamlit
st.pyplot(fig)
