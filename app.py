import streamlit as st
import psycopg2
from datetime import datetime

# --- LOGO E CABEÇALHO ---
ufba_logo_url = "https://imgs.search.brave.com/xr0SY0AP-69kIDcZ-TmUvmzvXluZp1HqcEOK0qmjtgU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy90/aHVtYi80LzQwL0Jy/YXMlQzMlQTNvX2Rh/X1VGQkEucG5nLzI1/MHB4LUJyYXMlQzMl/QTNvX2RhX1VGQkEu/cG5n"

st.set_page_config(page_title="Formulário TCC - Práticas Leitoras", layout="centered")

# Layout superior com logo e título
col1, col2 = st.columns([1, 5])
with col1:
    st.image(ufba_logo_url, width=100)
with col2:
    st.markdown("<h1 style='color:#004080;'>📚 Formulário de Pesquisa</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#555;'>Tecnologias e Práticas Leitoras - Estudantes Quilombolas da UFBA/UFRB</h3>", unsafe_allow_html=True)
    st.markdown("**Pesquisa para o TCC em Biblioteconomia e Documentação - UFBA**")

st.markdown("<h4 style='text-align: center; color:#800000;'>✊🏿 Resistência Quilombola ✊🏿</h4>", unsafe_allow_html=True)
st.markdown("---")

# PROBLEMA DE PESQUISA E OBJETIVO
with st.expander("🧠 PROBLEMA DE PESQUISA E OBJETIVO", expanded=True):
    st.markdown("**Problema de pesquisa:** Quais os reflexos das tecnologias de informação e comunicação nas práticas leitoras de jovens universitários quilombolas?")
    st.markdown("**Objetivo geral:** Compreender os reflexos das tecnologias de informação e comunicação nas práticas leitoras de jovens universitários quilombolas.")

# --- CONEXÃO COM BANCO DE DADOS ---
conn = psycopg2.connect(
    host="ep-royal-hall-acxwl5sf-pooler.sa-east-1.aws.neon.tech",
    dbname="questionario_tecnologia_praticas_leitoras",
    user="neondb_owner",
    password="npg_hCNPobG6KH2c",
    sslmode="require"
)
cursor = conn.cursor()

# --- FORMULÁRIO ---
with st.form("formulario"):
    st.markdown("### 🧑🏿‍🎓 Perfil do Universitário Quilombola")
    comunidade = st.text_input("Qual o nome da comunidade quilombola/Estado você nasceu?")

    universidade = st.radio("Qual universidade você está cursando:", [
        "Universidade Federal do Recôncavo da Bahia", "Universidade Federal da Bahia"
    ])

    cursos = [
        "História", "Filosofia", "Direito", "Economia", "Biblioteconomia", "Medicina", "Enfermagem",
        "Engenharia Civil", "Engenharia Ambiental", "Computação", "Pedagogia", "Letras", "Cinema",
        "BI de Humanidades", "Museologia", "BI de Artes", "BI de Saúde", "BI de Ciência e Tecnologia"
    ]
    curso = st.selectbox("Qual o curso que está matriculado:", cursos + ["Outro"])
    if curso == "Outro":
        curso = st.text_input("Especifique o curso")

    acesso_leitura = st.multiselect(
        "Como você acessava o livro e a leitura na comunidade quilombola que você nasceu:",
        ["biblioteca da comunidade", "biblioteca da escola", "biblioteca de uma amiga", "ponto de leitura da comunidade"]
    )

    st.markdown("### 🌐 Tecnologias de Informação e Comunicação")

    acesso_internet = st.radio("Como é o acesso à internet na comunidade onde você morava:", [
        "Muito bom", "Bom", "Regular", "Ruim", "Ótimo", "Não se aplica. Na comunidade onde morava não tem acesso à internet"
    ])

    anos_internet = st.radio("Há quantos anos a comunidade onde você morava dispõe de internet:", [
        "Menos de 2 anos", "De 2 a 5 anos", "De 5 a 8 anos", "Mais de 8 anos"
    ])

    equipamentos = st.multiselect("Na comunidade onde você morava, marque o(s) equipamento(s) que você utilizava para acessar o livro e a leitura antes da universidade:", [
        "Celular smartphone", "Computador/notebook pessoal", "Tablet", "E-reader (ex: Kindle)",
        "Computador compartilhado (família)", "Computador compartilhado (biblioteca)", "Não se aplica", "Outro"
    ])
    if "Outro" in equipamentos:
        outro_equipamento = st.text_input("Especifique o outro equipamento")
        equipamentos.append(outro_equipamento)

    avaliacao_tec_uni = st.radio("Como você avalia a disponibilização de recursos tecnológicos na universidade:", [
        "Muito bom", "Bom", "Regular", "Ruim", "Ótimo"
    ])

    st.markdown("### 📖 Práticas Leitoras")

    frequencia_acesso_livro = st.selectbox("Depois que ingressou na universidade, qual a frequência que você tem acesso ao livro e à leitura?", [
        "Diariamente", "Semanalmente", "Mensalmente", "Raramente"
    ])

    frequencia_leitura_textos = st.selectbox("Com que frequência você realiza leitura de textos longos (+20 páginas)?", [
        "Diariamente", "Semanalmente", "Mensalmente", "Raramente"
    ])

    impacto_tecnologia = st.radio("Como você avalia o impacto da tecnologia no acesso ao livro e à leitura:", [
        "Muito bom", "Bom", "Regular", "Ruim", "Ótimo"
    ])

    avaliacao_formacao = st.radio("Como você avalia o acesso que auxilia sua formação acadêmica:", [
        "Muito bom", "Bom", "Regular", "Ruim", "Ótimo",
        "Não se aplica. Na comunidade onde morava não tem acesso à internet"
    ])

    experiencia_antes = st.text_area("Compartilhe uma experiência com tecnologia e leitura antes da universidade")
    experiencia_depois = st.text_area("Compartilhe uma experiência com tecnologia e leitura depois da universidade")

    submit = st.form_submit_button("📩 Enviar Resposta")

    if submit:
        cursor.execute('''
            INSERT INTO respostas (
                comunidade_natal, universidade, curso, acesso_leitura_comunidade,
                acesso_internet_comunidade, anos_internet_comunidade,
                equipamentos_utilizados, avaliacao_tecnologia_universidade,
                frequencia_acesso_livro, frequencia_leitura_textos_longos,
                avaliacao_impacto_tecnologia, avaliacao_formacao_tecnologia,
                experiencia_antes_universidade, experiencia_depois_universidade,
                data_envio
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            comunidade, universidade, curso, ", ".join(acesso_leitura),
            acesso_internet, anos_internet, ", ".join(equipamentos),
            avaliacao_tec_uni, frequencia_acesso_livro, frequencia_leitura_textos,
            impacto_tecnologia, avaliacao_formacao,
            experiencia_antes, experiencia_depois, datetime.now()
        ))
        conn.commit()
        st.success("🎉 Sua resposta foi registrada com sucesso. Muito obrigado por contribuir com a pesquisa!")
