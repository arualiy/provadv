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

#Segundo gráfico

# Filtro para tipo de medalha
tipos_de_medalha = medalhistas['medal'].unique()
medalha_selecionada = st.selectbox('Escolha o tipo de medalha:', options=tipos_de_medalha)

# Filtrar medalhistas com base no tipo de medalha selecionada
medalhistas_filtrados = medalhistas[medalhistas['medal'] == medalha_selecionada]

# Mesclar medalhistas filtrados com esportes
medalhistas_esporte = pd.merge(medalhistas_filtrados, esportes, left_on='sport_id', right_on='sport_id')

# Agrupar o número de medalhistas por esporte
medalhistas_por_esporte = medalhistas_esporte.groupby('sport')['medalist_name'].count().reset_index()
medalhistas_por_esporte.columns = ['Esporte', 'Número de Medalhistas']

# Criar o gráfico de medalhistas por esporte
fig2, ax2 = plt.subplots(figsize=(10, 6))
medalhistas_por_esporte.plot(kind='bar', x='Esporte', y='Número de Medalhistas', color='green', ax=ax2)
ax2.set_title('Medalhistas por Esporte')
ax2.set_ylabel('Número de Medalhistas')
ax2.set_xlabel('Esporte')
ax2.set_xticklabels(medalhistas_por_esporte['Esporte'], rotation=90)

# Exibir o gráfico no Streamlit
st.pyplot(fig2)

# Exibir o gráfico no Streamlit
st.pyplot(fig)
