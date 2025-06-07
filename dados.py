import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(page_title="Dashboard: Tecnologia e Práticas Leitoras", layout="wide")
st.title("📊 Questionário - Tecnologia e Práticas Leitoras")
st.markdown("**Estudantes Quilombolas da UFBA**")

# --- CONEXÃO COM BANCO DE DADOS ---
conn = psycopg2.connect(
    host="ep-royal-hall-acxwl5sf-pooler.sa-east-1.aws.neon.tech",
    dbname="questionario_tecnologia_praticas_leitoras",
    user="neondb_owner",
    password="npg_hCNPobG6KH2c",
    sslmode="require"
)
cursor = conn.cursor()

# --- CONSULTA AOS DADOS ---
cursor.execute("SELECT * FROM respostas")
dados = cursor.fetchall()
colunas = [desc[0] for desc in cursor.description]
df = pd.DataFrame(dados, columns=colunas)

# --- GRÁFICOS INTERATIVOS ---

# CURSOS (mantém como histogram)
fig_curso = px.histogram(df, x="curso", title="Distribuição por Curso", color="curso")
st.plotly_chart(fig_curso, use_container_width=True)

# ACESSO À LEITURA NA COMUNIDADE (Bar horizontal)
fig_leitura = px.bar(df, y="acesso_leitura_comunidade", title="Formas de Acesso à Leitura na Comunidade", color="acesso_leitura_comunidade")
st.plotly_chart(fig_leitura, use_container_width=True)

# AVALIAÇÃO DO ACESSO À INTERNET (Pie)
fig_net_comunidade = px.pie(df, names="acesso_internet_comunidade", title="Avaliação do Acesso à Internet na Comunidade")
st.plotly_chart(fig_net_comunidade, use_container_width=True)

# TEMPO DE ACESSO À INTERNET (Bar)
fig_anos_net = px.bar(df, x="anos_internet_comunidade", color="anos_internet_comunidade", title="Tempo com Acesso à Internet")
st.plotly_chart(fig_anos_net, use_container_width=True)

# EQUIPAMENTOS UTILIZADOS (Treemap)
fig_equip = px.treemap(df, path=["equipamentos_utilizados"], title="Equipamentos Usados para Leitura")
st.plotly_chart(fig_equip, use_container_width=True)

# AVALIAÇÃO DOS RECURSOS TECNOLÓGICOS (Pie)
fig_avaliacao_tec_uni = px.pie(df, names="avaliacao_tecnologia_universidade", title="Recursos Tecnológicos na Universidade")
st.plotly_chart(fig_avaliacao_tec_uni, use_container_width=True)

# FREQUÊNCIA DE ACESSO AO LIVRO (Bar horizontal)
fig_freq_livros = px.bar(df, y="frequencia_acesso_livro", title="Frequência de Acesso ao Livro", color="frequencia_acesso_livro")
st.plotly_chart(fig_freq_livros, use_container_width=True)

# FREQUÊNCIA LEITURA TEXTOS LONGOS (Funnel)
fig_textos_longos = px.funnel(df, x="frequencia_leitura_textos_longos", y="frequencia_leitura_textos_longos", title="Frequência de Leitura de Textos Longos")
st.plotly_chart(fig_textos_longos, use_container_width=True)

# IMPACTO DA TECNOLOGIA (Pie)
fig_impacto_tec = px.pie(df, names="avaliacao_impacto_tecnologia", title="Impacto da Tecnologia no Acesso à Leitura")
st.plotly_chart(fig_impacto_tec, use_container_width=True)

# FORMAÇÃO ACADÊMICA E TECNOLOGIA (Bar)
fig_formacao = px.bar(df, x="avaliacao_formacao_tecnologia", color="avaliacao_formacao_tecnologia", title="Tecnologia e Formação Acadêmica")
st.plotly_chart(fig_formacao, use_container_width=True)

# --- TABELA COM TODOS OS DADOS ---
st.subheader("📋 Dados Brutos")
st.dataframe(df, use_container_width=True)
