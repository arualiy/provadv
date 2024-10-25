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

# Agrupar as medalhas por país
medalhas_por_pais = df.groupby('País')['Medalha'].count()

# Criar o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
medalhas_por_pais.plot(kind='barh', color='skyblue', ax=ax)
ax.set_title('Distribuição de Medalhas por País')
ax.set_xlabel('Número de Medalhas')
ax.set_ylabel('País')

# Exibir o gráfico no Streamlit
st.pyplot(fig)

# Filtro para tipo de medalha
tipos_de_medalha = medalhistas['medal'].unique()

medalha_selecionada = st.selectbox('Escolha o tipo de medalha:', options=tipos_de_medalha)
# Gerar gráficos de medalhistas por esporte
# Mesclar medalhistas com esportes
medalhistas_esporte = pd.merge(medalhistas, esportes, on='sport_id')

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
