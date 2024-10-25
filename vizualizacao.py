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
