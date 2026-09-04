import streamlit as st
import random

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Accuracy Music",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS / DESIGN
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #080810 0%,
        #111126 50%,
        #080810 100%
    );
    color: white;
}

.block-container {
    max-width: 1150px;
    padding-top: 25px;
    padding-bottom: 50px;
}

/* LOGO */

.logo {
    font-size: 30px;
    font-weight: 800;
    color: white;
}

.logo span {
    color: #8b5cf6;
}

/* HERO */

.hero {
    text-align: center;
    padding: 55px 20px 35px 20px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
    color: white;
}

.hero h1 span {
    color: #8b5cf6;
}

.hero p {
    font-size: 18px;
    color: #a1a1aa;
}

/* CARDS */

.card {
    background: rgba(24, 24, 40, 0.85);
    border: 1px solid rgba(139, 92, 246, 0.25);
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
}

.card-title {
    font-size: 23px;
    font-weight: 700;
    color: white;
    margin-bottom: 5px;
}

.card-description {
    color: #a1a1aa;
    font-size: 14px;
}

/* INPUTS */

input {
    background-color: #181825 !important;
    color: white !important;
}

div[data-baseweb="select"] > div {
    background-color: #181825;
    border-radius: 10px;
}

/* BOTÃO */

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: none;
    background: linear-gradient(
        90deg,
        #7c3aed,
        #8b5cf6
    );
    color: white;
    font-size: 17px;
    font-weight: 700;
    padding: 14px;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #6d28d9,
        #7c3aed
    );
}

/* RESULTADO */

.result-card {
    background: linear-gradient(
        145deg,
        rgba(124, 58, 237, 0.25),
        rgba(24, 24, 40, 0.95)
    );

    border: 1px solid rgba(139, 92, 246, 0.4);
    border-radius: 20px;
    padding: 35px;
    text-align: center;
    margin-top: 30px;
}

.score-label {
    color: #a1a1aa;
    font-size: 15px;
    letter-spacing: 1px;
}

.score {
    font-size: 70px;
    font-weight: 800;
    color: #a78bfa;
    margin: 5px 0;
}

.result-message {
    font-size: 20px;
    font-weight: 600;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #71717a;
    margin-top: 60px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOGO
# =========================================================

st.markdown("""
<div class="logo">
    🎵 Accuracy<span>Music</span>
</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <h1>
        Descubra o potencial da sua <span>música</span>
    </h1>

    <p>
        Informe as características da música ou envie um arquivo
        de áudio para realizar uma análise.
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INFORMAÇÕES DA MÚSICA
# =========================================================

st.markdown("""
<div class="card">

    <div class="card-title">
        🎧 Informações da música
    </div>

    <div class="card-description">
        Preencha as informações abaixo.
    </div>

</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)


# =========================================================
# COLUNA 1
# =========================================================

with col1:

    bpm = st.number_input(
        "BPM",
        min_value=40,
        max_value=250,
        value=120,
        step=1,
        help="Batidas por minuto."
    )

    genero = st.selectbox(
        "Gênero musical",
        [
            "Pop",
            "Rock",
            "Hip-Hop",
            "Rap",
            "R&B",
            "Eletrônica",
            "Funk",
            "Sertanejo",
            "Samba",
            "MPB",
            "Reggae",
            "Jazz",
            "Blues",
            "Clássica",
            "Outro"
        ]
    )

    duracao_minutos = st.number_input(
        "Duração — minutos",
        min_value=0,
        max_value=20,
        value=3,
        step=1
    )

    duracao_segundos = st.number_input(
        "Duração — segundos",
        min_value=0,
        max_value=59,
        value=30,
        step=1
    )


# =========================================================
# COLUNA 2
# =========================================================

with col2:

    instrumentos = st.multiselect(
        "Instrumentos utilizados",
        [
            "Piano",
            "Violão",
            "Guitarra",
            "Baixo",
            "Bateria",
            "Violino",
            "Saxofone",
            "Trompete",
            "Sintetizador",
            "Voz",
            "Ukulele",
            "Percussão",
            "Outro"
        ],
        default=["Voz"]
    )

    acustico = st.radio(
        "A música é acústica?",
        ["Sim", "Não"],
        horizontal=True
    )

    feat = st.radio(
        "Possui feat/parceria?",
        ["Sim", "Não"],
        horizontal=True
    )

    streaming = st.selectbox(
        "Streaming utilizado",
        [
            "Spotify",
            "YouTube Music",
            "Apple Music",
            "Amazon Music",
            "Deezer",
            "SoundCloud",
            "Outro"
        ]
    )


# =========================================================
# UPLOAD DA MÚSICA
# =========================================================

st.markdown("""
<div class="card">

    <div class="card-title">
        🎵 Arquivo da música
    </div>

    <div class="card-description">
        Envie o arquivo de áudio para que futuramente
        possamos extrair informações automaticamente.
    </div>

</div>
""", unsafe_allow_html=True)


arquivo_musica = st.file_uploader(
    "Escolha o arquivo de áudio",
    type=[
        "mp3",
        "wav",
        "m4a",
        "flac",
        "ogg"
    ],
    help="Formatos aceitos: MP3, WAV, M4A, FLAC e OGG."
)


# =========================================================
# MOSTRAR ARQUIVO
# =========================================================

if arquivo_musica is not None:

    st.success(
        f"Arquivo carregado: {arquivo_musica.name}"
    )

    st.audio(
        arquivo_musica
    )

    st.info(
        "O áudio foi carregado com sucesso. "
        "A transcrição e a extração automática de "
        "características serão adicionadas na próxima etapa."
    )


# =========================================================
# BOTÃO
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

analisar = st.button(
    "🎯 ANALISAR MÚSICA"
)


# =========================================================
# FUNÇÃO DE SIMULAÇÃO
# =========================================================

def gerar_resultado():

    # -----------------------------------------------------
    # ATENÇÃO:
    # ESTA FUNÇÃO É TEMPORÁRIA.
    #
    # Ela apenas simula uma previsão.
    #
    # Posteriormente vamos substituir isso pelo modelo
    # real de Machine Learning.
    # -----------------------------------------------------

    pontuacao = 50

    # BPM
    if 90 <= bpm <= 140:
        pontuacao += 8

    # Gêneros
    generos_favoraveis = [
        "Pop",
        "Hip-Hop",
        "Rap",
        "R&B",
        "Eletrônica",
        "Funk"
    ]

    if genero in generos_favoraveis:
        pontuacao += 7

    # Duração
    duracao_total = (
        duracao_minutos * 60
        + duracao_segundos
    )

    if 150 <= duracao_total <= 240:
        pontuacao += 8

    # Instrumentos
    if len(instrumentos) >= 2:
        pontuacao += 5

    # Acústico
    if acustico == "Sim":
        pontuacao += 2

    # Feat
    if feat == "Sim":
        pontuacao += 5

    # Arquivo enviado
    if arquivo_musica is not None:
        pontuacao += 5

    # Pequena variação
    pontuacao += random.randint(-5, 5)

    # Limitar entre 0 e 100
    pontuacao = max(
        0,
        min(100, pontuacao)
    )

    return pontuacao


# =========================================================
# RESULTADO
# =========================================================

if analisar:

    score = gerar_resultado()

    if score >= 80:

        mensagem = "🔥 Alto potencial de popularidade"

        descricao = (
            "As características informadas "
            "indicam um alto potencial."
        )

    elif score >= 60:

        mensagem = "🟢 Bom potencial de popularidade"

        descricao = (
            "A música apresenta características "
            "associadas a um bom potencial."
        )

    elif score >= 40:

        mensagem = "🟡 Potencial moderado"

        descricao = (
            "A música apresenta um potencial "
            "moderado de popularidade."
        )

    else:

        mensagem = "🔵 Potencial baixo"

        descricao = (
            "As características informadas "
            "resultaram em uma estimativa menor."
        )


    # =====================================================
    # CARD DE RESULTADO
    # =====================================================

    st.markdown(f"""
    <div class="result-card">

        <div class="score-label">
            POPULARIDADE ESTIMADA
        </div>

        <div class="score">
            {score}/100
        </div>

        <div class="result-message">
            {mensagem}
        </div>

        <p style="color:#a1a1aa;">
            {descricao}
        </p>

    </div>
    """, unsafe_allow_html=True)


    # =====================================================
    # RESUMO
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

        <div class="card-title">
            📊 Dados analisados
        </div>

    </div>
    """, unsafe_allow_html=True)


    r1, r2, r3, r4 = st.columns(4)


    with r1:

        st.metric(
            "BPM",
            bpm
        )


    with r2:

        st.metric(
            "Gênero",
            genero
        )


    with r3:

        st.metric(
            "Duração",
            f"{duracao_minutos}:{duracao_segundos:02d}"
        )


    with r4:

        st.metric(
            "Streaming",
            streaming
        )


    st.write(
        "**Instrumentos:**"
    )

    if instrumentos:

        st.write(
            ", ".join(instrumentos)
        )

    else:

        st.write(
            "Nenhum instrumento informado."
        )


    st.write(
        f"**Acústico:** {acustico}"
    )

    st.write(
        f"**Feat/Parceria:** {feat}"
    )


    if arquivo_musica is not None:

        st.write(
            f"**Arquivo:** {arquivo_musica.name}"
        )


# =========================================================
# RODAPÉ
# =========================================================

st.markdown("""
<div class="footer">

    Accuracy Music © 2026<br>
    Sistema de análise de popularidade musical

</div>
""", unsafe_allow_html=True)