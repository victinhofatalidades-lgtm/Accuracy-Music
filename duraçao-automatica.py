import random

import streamlit as st
from mutagen import File as MutagenFile


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
# FUNÇÕES AUXILIARES
# ============================================================

def obter_duracao_arquivo(arquivo):
    """Retorna a duração do áudio em segundos ou None se não for possível ler."""
    if arquivo is None:
        return None

    try:
        audio = MutagenFile(arquivo)
        if audio is not None and hasattr(audio, "info"):
            return round(audio.info.length)
    except Exception:
        return None
    finally:
        arquivo.seek(0)

    return None


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #090714 0%, #100b22 50%, #080611 100%);
        color: white;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    .main {
        padding-top: 20px;
    }

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

    .stSelectbox label,
    .stNumberInput label,
    .stMultiSelect label,
    .stRadio label,
    .stFileUploader label {
        color: #e5e1ec !important;
        font-weight: 600;
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 14px;
        background: linear-gradient(90deg, #7b3ff2, #a45cff);
        color: white;
        font-size: 17px;
        font-weight: 700;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(140, 75, 255, 0.35);
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown("## 🎵 Accuracy**Music**")
st.title("Descubra o potencial da sua música")
st.caption(
    "Informe as características da música ou envie um arquivo de áudio "
    "para realizar uma análise."
)


# ============================================================
# INFORMAÇÕES DA MÚSICA
# ============================================================

st.subheader("🎧 Informações da música")
st.caption("Preencha as informações abaixo.")
st.divider()

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
            "Rock", "Rock Alternativo", "Hard Rock", "Punk Rock", "Indie Rock",
            "Pop Rock", "Grunge", "Rock Psicodélico",
            "Pop", "Synthpop", "Electropop", "Dance Pop", "Indie Pop", "K-Pop",
            "J-Pop", "Pop Latino",
            "Hip-Hop", "Rap", "Trap", "Drill", "Boom Bap", "Gangsta Rap",
            "Conscious Rap", "Lo-fi Hip-Hop",
            "Eletrônica", "House", "Deep House", "Tech House", "Techno", "Trance",
            "Dubstep", "Drum & Bass", "EDM", "Future Bass",
            "Jazz", "Bebop", "Swing", "Smooth Jazz", "Jazz Fusion", "Free Jazz",
            "Música Clássica", "Barroco", "Romântica", "Ópera", "Sinfônica",
            "Blues", "Delta Blues", "Chicago Blues", "Electric Blues", "Blues Rock",
            "Country", "Country Pop", "Bluegrass", "Outlaw Country", "Country Rock",
            "Latin", "Reggaeton", "Salsa", "Bachata", "Merengue", "Latin Pop",
            "Música Brasileira", "MPB", "Sertanejo", "Funk Brasileiro", "Pagode",
            "Samba", "Forró", "Bossa Nova", "Axé",
            "R&B", "Contemporary R&B", "Neo Soul", "Soul", "Funk Soul", "Motown",
            "Reggae", "Dancehall", "Dub", "Ska",
            "Metal", "Heavy Metal", "Thrash Metal", "Death Metal", "Black Metal", "Metalcore",
            "Folk", "Indie Folk", "Folk Rock", "Acoustic Folk", "Contemporary Folk",
            "Gospel", "Contemporary Gospel", "Gospel Rock", "Gospel R&B", "Outro"
        ]
    )

with col3:
    streaming = st.selectbox(
        "Streaming usado",
        [
            "Spotify", "YouTube Music", "Apple Music", "Amazon Music",
            "Deezer", "SoundCloud", "Outro"
        ]
    )


# ============================================================
# ARQUIVO DE ÁUDIO E DURAÇÃO AUTOMÁTICA
# ============================================================

st.subheader("🎵 Arquivo da música")
st.caption("Envie o áudio para identificar sua duração automaticamente.")
st.divider()

arquivo_musica = st.file_uploader(
    "Escolha o arquivo de áudio",
    type=["mp3", "wav", "m4a", "flac", "ogg"],
    help="Formatos aceitos: MP3, WAV, M4A, FLAC e OGG."
)

duracao_arquivo = obter_duracao_arquivo(arquivo_musica)

if arquivo_musica is not None:
    st.success(f"Arquivo carregado: {arquivo_musica.name}")
    st.audio(arquivo_musica)

    if duracao_arquivo is not None:
        st.success("Duração identificada automaticamente a partir do arquivo.")
    else:
        st.warning(
            "Não foi possível identificar a duração do arquivo. "
            "Envie outro arquivo em um dos formatos aceitos."
        )


# ============================================================
# DURAÇÃO
# ============================================================

st.subheader("⏱️ Duração")
st.divider()

if duracao_arquivo is not None:
    minutos = duracao_arquivo // 60
    segundos = duracao_arquivo % 60

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Minutos identificados", minutos)
    with col2:
        st.metric("Segundos identificados", f"{segundos:02d}")

    duracao_segundos = duracao_arquivo
else:
    minutos = 0
    segundos = 0
    duracao_segundos = None
    st.info("Envie um arquivo de áudio para identificar a duração automaticamente.")


# ============================================================
# INSTRUMENTOS
# ============================================================

st.subheader("🎸 Instrumentos")
st.caption("Selecione os instrumentos presentes na música.")
st.divider()

instrumentos = st.multiselect(
    "Instrumentos utilizados",
    [
        "Violão", "Guitarra", "Guitarra elétrica", "Guitarra acústica", "Baixo",
        "Contrabaixo", "Ukulele", "Banjo", "Bandolim", "Cavaquinho", "Harpa",
        "Violino", "Viola", "Violoncelo",
        "Piano", "Teclado", "Órgão", "Acordeon", "Sanfona", "Sintetizador",
        "Rhodes", "Cravo",
        "Bateria", "Percussão", "Cajón", "Congas", "Bongôs", "Timbales",
        "Pandeiro", "Tamborim", "Atabaque", "Berimbau", "Triângulo", "Xilofone",
        "Marimba",
        "Flauta", "Flauta doce", "Clarinete", "Oboé", "Fagote", "Saxofone",
        "Trompete", "Trombone", "Tuba", "Trompa",
        "Voz", "Coral", "Beatbox", "Drum Machine", "Sampler", "Turntable/DJ",
        "Loops eletrônicos", "Outro"
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
# FUNÇÃO DE PREVISÃO (SIMULAÇÃO)
# ============================================================

def gerar_resultado():
    score = 50

    if 90 <= bpm <= 140:
        score += 10
    elif 70 <= bpm <= 160:
        score += 5
    else:
        score -= 3

    generos_favoraveis = [
        "Pop", "Hip-Hop", "Rap", "R&B", "Eletrônica", "Funk Brasileiro"
    ]

    if genero in generos_favoraveis:
        score += 8

    if 150 <= duracao_segundos <= 240:
        score += 8
    elif 120 <= duracao_segundos <= 300:
        score += 4
    else:
        score -= 2

    if len(instrumentos) >= 3:
        score += 5
    elif len(instrumentos) == 2:
        score += 3

    if acustico == "Sim":
        score += 2

    if feat == "Sim":
        score += 5

    if arquivo_musica is not None:
        score += 3

    score += random.randint(-5, 5)

    return max(0, min(100, score))


# ============================================================
# BOTÃO ANALISAR
# ============================================================

st.write("")

if st.button("🚀 ANALISAR MÚSICA", disabled=duracao_segundos is None):
    score = gerar_resultado()

    if score >= 80:
        categoria = "🔥 Alto potencial de popularidade"
    elif score >= 60:
        categoria = "🟢 Bom potencial de popularidade"
    elif score >= 40:
        categoria = "🟡 Potencial moderado"
    else:
        categoria = "🔵 Potencial baixo"

    st.subheader("📈 Resultado da análise")
    st.metric("Potencial de popularidade", f"{score}/100")
    st.success(categoria)

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
    st.write(
        f"**Arquivo:** {arquivo_musica.name}"
        if arquivo_musica else "**Arquivo:** Nenhum arquivo enviado"
    )


# ============================================================
# RODAPÉ
# ============================================================

st.divider()
st.caption(
    "Accuracy Music © 2026 — Projeto acadêmico de Ciência de Dados e Machine Learning"
)
