import streamlit as st
import random

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Accuracy Music",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

    /* Fundo geral */
    .stApp {
        background: linear-gradient(
            135deg,
            #090714 0%,
            #100b22 50%,
            #080611 100%
        );
        color: white;
    }

    /* Remove elementos padrão */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Container principal */
    .main {
        padding-top: 20px;
    }

    /* Títulos e textos */
    h1 {
        text-align: center;
        color: #ffffff !important;
        margin-bottom: 10px;
    }

    h2, h3 {
        color: #ffffff !important;
    }

    .stCaption {
        color: #bdb8ca !important;
    }

    /* Inputs */
    .stSelectbox label,
    .stNumberInput label,
    .stMultiSelect label,
    .stRadio label,
    .stFileUploader label {
        color: #e5e1ec !important;
        font-weight: 600;
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
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(140, 75, 255, 0.35);
    }


    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #777184;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)

# ============================================================
# LOGO
# ============================================================

st.markdown("## 🎵 Accuracy**Music**")

# ============================================================
# HERO
# ============================================================

st.title("Descubra o potencial da sua música")
st.caption("Informe as características da música ou envie um arquivo de áudio para realizar uma análise.")

# ============================================================
# INFORMAÇÕES DA MÚSICA
# ============================================================

st.subheader("🎧 Informações da música")
st.caption("Preencha as informações abaixo.")
st.divider()

# ============================================================
# PRIMEIRA LINHA
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
            # ROCK
            "Rock",
            "Rock Alternativo",
            "Hard Rock",
            "Punk Rock",
            "Indie Rock",
            "Pop Rock",
            "Grunge",
            "Rock Psicodélico",

            # POP
            "Pop",
            "Synthpop",
            "Electropop",
            "Dance Pop",
            "Indie Pop",
            "K-Pop",
            "J-Pop",
            "Pop Latino",

            # HIP-HOP / RAP
            "Hip-Hop",
            "Rap",
            "Trap",
            "Drill",
            "Boom Bap",
            "Gangsta Rap",
            "Conscious Rap",
            "Lo-fi Hip-Hop",

            # ELETRÔNICA
            "Eletrônica",
            "House",
            "Deep House",
            "Tech House",
            "Techno",
            "Trance",
            "Dubstep",
            "Drum & Bass",
            "EDM",
            "Future Bass",

            # JAZZ
            "Jazz",
            "Bebop",
            "Swing",
            "Smooth Jazz",
            "Jazz Fusion",
            "Free Jazz",

            # CLÁSSICA
            "Música Clássica",
            "Barroco",
            "Romântica",
            "Ópera",
            "Sinfônica",

            # BLUES
            "Blues",
            "Delta Blues",
            "Chicago Blues",
            "Electric Blues",
            "Blues Rock",

            # COUNTRY
            "Country",
            "Country Pop",
            "Bluegrass",
            "Outlaw Country",
            "Country Rock",

            # LATIN
            "Latin",
            "Reggaeton",
            "Salsa",
            "Bachata",
            "Merengue",
            "Latin Pop",

            # MÚSICA BRASILEIRA
            "Música Brasileira",
            "MPB",
            "Sertanejo",
            "Funk Brasileiro",
            "Pagode",
            "Samba",
            "Forró",
            "Bossa Nova",
            "Axé",

            # R&B / SOUL
            "R&B",
            "Contemporary R&B",
            "Neo Soul",
            "Soul",
            "Funk Soul",
            "Motown",

            # REGGAE
            "Reggae",
            "Dancehall",
            "Dub",
            "Ska",

            # METAL
            "Metal",
            "Heavy Metal",
            "Thrash Metal",
            "Death Metal",
            "Black Metal",
            "Metalcore",

            # FOLK
            "Folk",
            "Indie Folk",
            "Folk Rock",
            "Acoustic Folk",
            "Contemporary Folk",

            # GOSPEL
            "Gospel",
            "Contemporary Gospel",
            "Gospel Rock",
            "Gospel R&B",

            # OUTROS
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
st.divider()

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
st.caption("Selecione os instrumentos presentes na música.")
st.divider()

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
st.caption("Informe algumas características adicionais da música.")
st.divider()

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
st.caption("Envie o arquivo de áudio para que futuramente possamos extrair informações automaticamente.")
st.divider()

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

    st.info(
        "A análise automática do áudio será integrada "
        "ao modelo de Machine Learning em uma próxima etapa."
    )

# ============================================================
# FUNÇÃO DE PREVISÃO
# ============================================================

def gerar_resultado():

    # --------------------------------------------------------
    # ATENÇÃO:
    # Esta função é apenas uma SIMULAÇÃO.
    # Depois iremos substituir pelo modelo real do TCC.
    # --------------------------------------------------------

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

    # Arquivo de áudio
    if arquivo_musica is not None:
        score += 3

    # Pequena variação aleatória
    score += random.randint(-5, 5)

    # Limita entre 0 e 100
    score = max(0, min(100, score))

    return score


# ============================================================
# BOTÃO ANALISAR
# ============================================================

st.write("")

if st.button("🚀 ANALISAR MÚSICA"):

    score = gerar_resultado()

    # --------------------------------------------------------
    # CLASSIFICAÇÃO
    # --------------------------------------------------------

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

    st.subheader("📈 Resultado da análise")
    st.metric("Potencial de popularidade", f"{score}/100")
    st.success(categoria)

    # ========================================================
    # MÉTRICAS
    # ========================================================

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("BPM", bpm)

    with col2:
        st.metric("Duração", f"{minutos}:{segundos:02d}")

    with col3:
        st.metric("Instrumentos", len(instrumentos))

    with col4:
        st.metric("Gênero", genero)

    # ========================================================
    # DETALHES
    # ========================================================

    st.write("")

    st.subheader("📊 Detalhes da análise")

    st.write(f"**Gênero:** {genero}")
    st.write(f"**Streaming:** {streaming}")
    st.write(f"**BPM:** {bpm}")
    st.write(f"**Duração:** {minutos}:{segundos:02d}")
    st.write(
        f"**Instrumentos:** "
        f"{', '.join(instrumentos) if instrumentos else 'Nenhum informado'}"
    )
    st.write(f"**Acústico:** {acustico}")
    st.write(f"**Feat/parceria:** {feat}")

    if arquivo_musica:
        st.write(f"**Arquivo:** {arquivo_musica.name}")
    else:
        st.write("**Arquivo:** Nenhum arquivo enviado")


# ============================================================
# RODAPÉ
# ============================================================

st.divider()
st.caption("Accuracy Music © 2026 — Projeto acadêmico de Ciência de Dados e Machine Learning")
