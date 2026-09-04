import streamlit as st
import random

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Accuracy Music",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS - APENAS ESTILO
# ============================================================

st.markdown("""
<style>

    /* Fundo */
    .stApp {
        background: linear-gradient(
            135deg,
            #090714 0%,
            #100b22 50%,
            #080611 100%
        );
        color: white;
    }

    /* Esconder menu padrão */
    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Texto geral */
    h1, h2, h3 {
        color: white !important;
    }

    /* Logo */
    .logo-text {
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 30px;
    }

    /* Destaque roxo */
    .purple-text {
        color: #a66cff;
    }

    /* Hero */
    .hero-box {
        background: rgba(25, 20, 38, 0.80);
        border: 1px solid rgba(155, 92, 255, 0.35);
        border-radius: 20px;
        padding: 40px 25px;
        margin-bottom: 30px;
        text-align: center;
    }

    /* Título */
    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 15px;
    }

    /* Descrição */
    .hero-description {
        font-size: 17px;
        color: #bdb8ca;
    }

    /* Separadores */
    hr {
        border-color: rgba(155, 92, 255, 0.25);
    }

    /* Labels */
    label {
        color: #e5e1ec !important;
    }

    /* Botão */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 14px;
        background: linear-gradient(
            90deg,
            #7b3ff2,
            #a45cff
        );
        color: white;
        font-size: 17px;
        font-weight: 700;
    }

    .stButton > button:hover {
        box-shadow: 0 8px 25px rgba(140, 75, 255, 0.35);
    }

    /* Resultado */
    .score-box {
        background: rgba(30, 23, 48, 0.90);
        border: 1px solid rgba(166, 108, 255, 0.45);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin-top: 25px;
    }

    .score-number {
        font-size: 70px;
        font-weight: 800;
        color: #a66cff;
    }

    .score-label {
        color: #bdb8ca;
        font-size: 15px;
    }

    .score-result {
        color: white;
        font-size: 23px;
        font-weight: 700;
        margin-top: 10px;
    }

    /* Métricas */
    .metric-box {
        background: rgba(23, 20, 32, 0.85);
        border: 1px solid rgba(155, 92, 255, 0.30);
        border-radius: 15px;
        padding: 18px;
        text-align: center;
    }

    .metric-number {
        color: #a66cff;
        font-size: 25px;
        font-weight: 700;
    }

    .metric-name {
        color: #aaa4b7;
        font-size: 13px;
    }

    /* Rodapé */
    .footer-text {
        text-align: center;
        color: #777184;
        margin-top: 50px;
        padding: 20px;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)

# ============================================================
# LOGO
# ============================================================

st.markdown(
    '<div class="logo-text">🎵 Accuracy<span class="purple-text">Music</span></div>',
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero-box">

    <div class="hero-title">
        Descubra o potencial da sua
        <span class="purple-text"> música</span>
    </div>

    <div class="hero-description">
        Informe as características da música ou envie um arquivo
        de áudio para realizar uma análise.
    </div>

</div>
""", unsafe_allow_html=True)

# ============================================================
# INFORMAÇÕES DA MÚSICA
# ============================================================

st.subheader("🎧 Informações da música")
st.caption("Preencha as informações abaixo.")

st.divider()

# ============================================================
# DADOS PRINCIPAIS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    bpm = st.number_input(
        "BPM",
        min_value=40,
        max_value=250,
        value=120,
        step=1,
        help="Batidas por minuto da música."
    )

with col2:

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

with col3:

    streaming = st.selectbox(
        "Streaming usado",
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

# ============================================================
# DURAÇÃO
# ============================================================

st.subheader("⏱️ Duração")

col1, col2 = st.columns(2)

with col1:

    minutos = st.number_input(
        "Minutos",
        min_value=0,
        max_value=20,
        value=3,
        step=1
    )

with col2:

    segundos = st.number_input(
        "Segundos",
        min_value=0,
        max_value=59,
        value=30,
        step=1
    )

duracao_segundos = (minutos * 60) + segundos

# ============================================================
# INSTRUMENTOS
# ============================================================

st.subheader("🎸 Instrumentos")

st.caption(
    "Selecione os instrumentos presentes na música."
)

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
    ]
)

# ============================================================
# CARACTERÍSTICAS
# ============================================================

st.subheader("🎛️ Características")

col1, col2 = st.columns(2)

with col1:

    acustico = st.radio(
        "A música é acústica?",
        ["Sim", "Não"],
        horizontal=True
    )

with col2:

    feat = st.radio(
        "Possui feat/parceria?",
        ["Sim", "Não"],
        horizontal=True
    )

# ============================================================
# ARQUIVO DE ÁUDIO
# ============================================================

st.subheader("🎵 Arquivo da música")

st.caption(
    "Envie o arquivo de áudio para análise."
)

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

if arquivo_musica is not None:

    st.success(
        f"Arquivo carregado: {arquivo_musica.name}"
    )

    st.audio(arquivo_musica)

# ============================================================
# FUNÇÃO DE PREVISÃO
# ============================================================

def gerar_resultado():

    # ========================================================
    # SIMULAÇÃO
    #
    # ATENÇÃO:
    # Esta parte será substituída pelo algoritmo real
    # de Machine Learning do TCC.
    # ========================================================

    score = 50

    # BPM
    if 90 <= bpm <= 140:
        score += 10

    elif 70 <= bpm <= 160:
        score += 5

    else:
        score -= 3

    # Gênero
    generos_favoraveis = [
        "Pop",
        "Hip-Hop",
        "Rap",
        "R&B",
        "Eletrônica",
        "Funk"
    ]

    if genero in generos_favoraveis:
        score += 8

    # Duração
    if 150 <= duracao_segundos <= 240:
        score += 8

    elif 120 <= duracao_segundos <= 300:
        score += 4

    else:
        score -= 2

    # Instrumentos
    if len(instrumentos) >= 3:
        score += 5

    elif len(instrumentos) == 2:
        score += 3

    # Acústico
    if acustico == "Sim":
        score += 2

    # Feat
    if feat == "Sim":
        score += 5

    # Arquivo
    if arquivo_musica is not None:
        score += 3

    # Pequena variação
    score += random.randint(-5, 5)

    # Limitar entre 0 e 100
    score = max(0, min(100, score))

    return score


# ============================================================
# BOTÃO
# ============================================================

st.divider()

if st.button("🚀 ANALISAR MÚSICA"):

    score = gerar_resultado()

    # ========================================================
    # CLASSIFICAÇÃO
    # ========================================================

    if score >= 80:

        categoria = "🔥 Alto potencial de popularidade"

    elif score >= 60:

        categoria = "🟢 Bom potencial de popularidade"

    elif score >= 40:

        categoria = "🟡 Potencial moderado"

    else:

        categoria = "🔵 Potencial baixo"

    # ========================================================
    # RESULTADO
    # ========================================================

    st.markdown(
        f"""
        <div class="score-box">

            <div class="score-label">
                POTENCIAL DE POPULARIDADE
            </div>

            <div class="score-number">
                {score}
            </div>

            <div class="score-label">
                de 100
            </div>

            <div class="score-result">
                {categoria}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # MÉTRICAS
    # ========================================================

    st.subheader("📊 Resumo da música")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "BPM",
            bpm
        )

    with col2:

        st.metric(
            "Duração",
            f"{minutos}:{segundos:02d}"
        )

    with col3:

        st.metric(
            "Instrumentos",
            len(instrumentos)
        )

    with col4:

        st.metric(
            "Gênero",
            genero
        )

    # ========================================================
    # DETALHES
    # ========================================================

    st.subheader("📋 Detalhes da análise")

    st.write(f"**Gênero:** {genero}")

    st.write(f"**Streaming:** {streaming}")

    st.write(f"**BPM:** {bpm}")

    st.write(
        f"**Duração:** {minutos}:{segundos:02d}"
    )

    if instrumentos:

        st.write(
            "**Instrumentos:** "
            + ", ".join(instrumentos)
        )

    else:

        st.write(
            "**Instrumentos:** Nenhum informado"
        )

    st.write(
        f"**Acústico:** {acustico}"
    )

    st.write(
        f"**Feat/parceria:** {feat}"
    )

    if arquivo_musica is not None:

        st.write(
            f"**Arquivo:** {arquivo_musica.name}"
        )

    else:

        st.write(
            "**Arquivo:** Nenhum arquivo enviado"
        )

# ============================================================
# RODAPÉ
# ============================================================

st.markdown(
    """
    <div class="footer-text">
        Accuracy Music © 2026
        <br>
        Projeto acadêmico de Ciência de Dados e Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)
