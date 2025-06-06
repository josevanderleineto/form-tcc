import streamlit as st

st.set_page_config(page_title="Questionário - Tecnologia e Práticas Leitoras", layout="centered")

st.title("📚 QUESTIONÁRIO - TECNOLOGIA E PRÁTICAS LEITORAS")
st.subheader("Estudantes Quilombolas da UFBA")

st.markdown("### PERFIL DO UNIVERSITÁRIO QUILOMBOLA")

nome_comunidade = st.text_input("1️⃣ Qual o nome da comunidade quilombola/Estado você nasceu?", key="comunidade")
universidade = st.selectbox("2️⃣ Qual universidade você está cursando?", 
    ["Universidade Federal do Recôncavo da Bahia", "Universidade Federal da Bahia"], key="universidade")

cursos = [
    "História", "Filosofia", "Direito", "Economia", "Biblioteconomia", "Medicina", "Enfermagem",
    "Engenharia Civil", "Engenharia Ambiental", "Computação", "Pedagogia", "Letras", "Cinema",
    "BI de Humanidades", "Museologia", "BI de Artes", "BI de Saúde", "BI de Ciência e Tecnologia", "Outro"
]
curso = st.selectbox("3️⃣ Qual o curso que está matriculado:", cursos, key="curso")

if curso == "Outro":
    outro_curso = st.text_input("Especifique o curso:", key="outro_curso")

acesso_leitura = st.multiselect("4️⃣ Como você acessava o livro e a leitura na comunidade quilombola que você nasceu?", 
    ["Biblioteca da comunidade", "Biblioteca da escola", "Biblioteca de uma amiga", "Ponto de leitura da comunidade"], key="acesso_leitura")

st.markdown("### TECNOLOGIA DE INFORMAÇÃO E COMUNICAÇÃO")

internet_comunidade = st.radio("5️⃣ Como é o acesso à internet na comunidade onde você morava?", 
    ["Muito bom", "Bom", "Regular", "Ruim", "Ótimo", "Não se aplica. Na comunidade onde morava não tem acesso à internet"], key="internet")

tempo_internet = st.radio("6️⃣ Há quantos anos a comunidade onde você morava dispõe de internet?", 
    ["Menos de 2 anos", "De 2 a 5 anos", "De 5 anos a 8 anos", "Mais de 8 anos"], key="tempo_internet")

equipamentos = st.multiselect("7️⃣ Marque o(s) equipamento(s) que você utilizava para acessar o livro e a leitura antes da universidade:", 
    ["Celular smartphone", "Computador/notebook pessoal", "Tablet", "E-reader (ex: Kindle)", 
     "Computador compartilhado (família)", "Computador compartilhado (biblioteca)", "Outro", "Não se aplica"], key="equipamentos")

if "Outro" in equipamentos:
    outro_equipamento = st.text_input("Se escolheu 'Outro', especifique:", key="outro_equipamento")

avaliacao_universidade = st.radio("8️⃣ Como você avalia a disponibilização de recursos tecnológicos para leitura na universidade?", 
    ["Muito bom", "Bom", "Regular", "Ruim", "Ótimo"], key="avaliacao_uni")

st.markdown("### PRÁTICAS LEITORAS")

frequencia_leitura = st.multiselect("9️⃣ Depois que ingressou na universidade, qual a frequência que você tem acesso ao livro e a leitura?", 
    ["Todos os dias", "Semanalmente", "Mensalmente", "Somente quando solicitado em aula"], key="frequencia")

frequencia_texto_longo = st.radio("🔟 Com que frequência você realiza leitura de textos longos (+20 páginas)?", 
    ["Diariamente", "Semanalmente", "Mensalmente", "Raramente", "Nunca"], key="texto_longo")

impacto_tic = st.radio("1️⃣1️⃣ Como você avalia o impacto da tecnologia no acesso ao livro e à leitura?", 
    ["Muito bom", "Bom", "Regular", "Ruim", "Ótimo"], key="impacto_tic")

avaliacao_tic_formacao = st.radio("1️⃣2️⃣ Como você avalia o acesso ao livro/leitura que auxiliam sua formação com TICs?", 
    ["Muito bom", "Bom", "Regular", "Ruim", "Ótimo", "Não se aplica. Na comunidade onde morava não tem acesso à internet"], key="avaliacao_tic_formacao")

st.markdown("### 📝 EXPERIÊNCIAS COM TECNOLOGIA E LEITURA")

experiencia_antes = st.text_area("1️⃣3️⃣ Compartilhe uma experiência antes de entrar na universidade:", key="antes_uni")
experiencia_depois = st.text_area("1️⃣4️⃣ Compartilhe uma experiência depois de entrar na universidade:", key="depois_uni")

# Enviar respostas
if st.button("📤 Enviar Respostas"):
    st.success("Respostas enviadas com sucesso! Obrigado por participar ✨")

