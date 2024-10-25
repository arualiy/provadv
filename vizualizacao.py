import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
medalhistas = pd.read_csv(r'medalists.csv')
paises = pd.read_csv(r'countries.csv')
delegacoes = pd.read_csv(r'delegations.csv')
medalhas = pd.read_csv(r'medals.csv')
esportes = pd.read_csv(r'sports.csv')

# Mesclar medalhistas com países
df = pd.merge(medalhistas, paises, left_on='country_id', right_on='country_id')[['medal', 'country_name']]
df.columns = ['Medalha', 'País']

# Agrupar as medalhas por país
medalhas_por_pais = df.groupby('País')['Medalha'].count().reset_index()
medalhas_por_pais.columns = ['País', 'Número de Medalhas']

# Criar um seletor para escolher o número de países a serem exibidos
num_paises = st.slider('Escolha o número de países a serem exibidos:', 
                       min_value=1, max_value=len(medalhas_por_pais), value=5)

# Ordenar e selecionar os países com mais medalhas
medalhas_selecionadas = medalhas_por_pais.nlargest(num_paises, 'Número de Medalhas')

# Criar o gráfico de medalhas por país
fig, ax = plt.subplots(figsize=(10, 6))
medalhas_selecionadas.plot(kind='barh', x='País', y='Número de Medalhas', color='skyblue', ax=ax)
ax.set_title('Distribuição de Medalhas por País')
ax.set_xlabel('Número de Medalhas')
ax.set_ylabel('País')

# Exibir o gráfico no Streamlit
st.pyplot(fig)
