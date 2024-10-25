import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# Carregar os dados
medalhistas = pd.read_csv(r'medalists.csv')
paises = pd.read_csv(r'countries.csv')
delegacoes = pd.read_csv(r'delegations.csv')
medalhas = pd.read_csv(r'medals.csv')
esportes = pd.read_csv(r'sports.csv')
lugar_nascimento = pd.read_csv(r'birthplace.csv')

# Mesclar medalhistas com países
df = pd.merge(medalhistas, paises, on='country_id')[['medal', 'country_name']]
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

# Segundo gráfico
# Filtro para tipo de medalha
tipos_de_medalha = medalhistas['medal'].unique()
medalha_selecionada = st.selectbox('Escolha o tipo de medalha:', options=tipos_de_medalha)

# Filtrar medalhistas com base no tipo de medalha selecionada
medalhistas_filtrados = medalhistas[medalhistas['medal'] == medalha_selecionada]

# Mesclar medalhistas filtrados com esportes
medalhistas_esporte = pd.merge(medalhistas_filtrados, esportes, on='sport_id')

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

#Grafico 3 
# Mesclar medalistas com locais de nascimento
merged_df = pd.merge(medalhistas, lugar_nascimento, on='birthplace_id', how='left')

# Adicionar coluna para continente (você deve ter uma coluna de continente ou fazer uma correspondência)
# Exemplo simplificado: Supondo que você tenha um mapeamento de países para continentes
country_to_continent = {
    'USA': 'North America',
    'BRA': 'South America',
    'CHN': 'Asia',
    'GBR': 'Europe',
    # Adicione mais países e seus continentes aqui
}

# Mapear os países para continentes
merged_df['continent'] = merged_df['country_id'].map(country_to_continent)

# Streamlit para filtros
st.title('Mapa de Dispersão de Medalhistas por Continente')

# Seleção de continente
continents = merged_df['continent'].dropna().unique()
selected_continent = st.selectbox('Escolha o continente:', options=continents)

# Filtrar dados pelo continente selecionado
filtered_df = merged_df[merged_df['continent'] == selected_continent]

# Criar o gráfico de dispersão
fig = px.scatter_geo(filtered_df,
                     lat='lat',
                     lon='lon',
                     text='medalist_name',  # texto para exibir ao passar o mouse
                     hover_name='medalist_name',
                     hover_data=['country_id', 'medal'],
                     title=f'Medalhistas de {selected_continent}',
                     projection='natural earth')

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)

