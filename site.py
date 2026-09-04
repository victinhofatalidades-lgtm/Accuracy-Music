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

    /* Logo */
    .logo {
        font-size: 28px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 30px;
    }

    .logo span {
        color: #9b5cff;
    }

    /* Hero */
    .hero {
        text-align: center;
        padding: 45px 20px;
        margin-bottom: 30px;
        border-radius: 20px;
        background: rgba(25, 20, 38, 0.75);
        border: 1px solid rgba(155, 92, 255, 0.35);
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 15px;
        color: white;
    }

    .hero h1 span {
        color: #a66cff;
    }

    .hero p {
        font-size: 17px;
        color: #bdb8ca;
        margin: 0;
    }

    /* Cards */
    .card {
        background: rgba(23, 20, 32, 0.85);
        border: 1px solid rgba(155, 92, 255, 0.30);
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 21px;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
    }

    .card-description {
        font-size: 14px;
        color: #aaa4b7;
        margin-bottom: 20px;
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

    /* Resultado */
    .result-card {
        text-align: center;
        background: linear-gradient(
            135deg,
            rgba(45, 28, 75, 0.9),
            rgba(25, 19, 42, 0.95)
        );
        border: 1px solid rgba(166, 108, 255, 0.45);
        border-radius: 20px;
        padding: 35px;
        margin-top: 25px;
    }

    .score {
        font-size: 72px;
        font-weight: 800;
        color: #a66cff;
        margin: 10px 0;
    }

    .score-label {
        color: #bdb8ca;
        font-size: 15px;
    }

    .result-title {
        font-size: 24px;
        font-weight: 700;
        color: white;
        margin-top: 10px;
    }

    /* Métricas */
    .metric-card {
        background: rgba(20, 17, 29, 0.8);
        border: 1px solid rgba(155, 92, 255, 0.25);
        border-radius: 14px;
        padding: 18px;
        text-align: center;
    }

    .metric-number {
        font-size: 25px;
        font-weight: 700;
        color: #a66cff;
    }

    .metric-text {
        font-size: 13px;
        color: #aaa4b7;
    }

    /* Rodapé */
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

st.markdown("""
<div class="logo">
    🎵 Accuracy<span>Music</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# HERO
# ============================================================

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

# ============================================================
# INFORMAÇÕES DA MÚSICA
# ============================================================

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

st.markdown("""
<div class="card">
    <div class="card-title">
        ⏱️ Duração
    </div>
</div>
""", unsafe_allow_html=True)

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

st.markdown("""
<div class="card">
    <div class="card-title">
        🎸 Instrumentos
    </div>

    <div class="card-description">
        Selecione os instrumentos presentes na música.
    </div>
</div>
""", unsafe_allow_html=True)

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

st.markdown("""
<div class="card">
    <div class="card-title">
        🎛️ Características
    </div>

    <div class="card-description">
        Informe algumas características adicionais da música.
    </div>
</div>
""", unsafe_allow_html=True)

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

st.markdown("<br>", unsafe_allow_html=True)

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

    st.markdown(f"""
    <div class="result-card">

        <div class="score-label">
            POTENCIAL DE POPULARIDADE
        </div>

        <div class="score">
            {score}
        </div>

        <div class="score-label">
            de 100
        </div>

        <div class="result-title">
            {categoria}
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ========================================================
    # MÉTRICAS
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">
                {bpm}
            </div>
            <div class="metric-text">
                BPM
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">
                {minutos}:{segundos:02d}
            </div>
            <div class="metric-text">
                Duração
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">
                {len(instrumentos)}
            </div>
            <div class="metric-text">
                Instrumentos
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">
                {genero}
            </div>
            <div class="metric-text">
                Gênero
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ========================================================
    # DETALHES
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

        <div class="card-title">
            📊 Detalhes da análise
        </div>

    </div>
    """, unsafe_allow_html=True)

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

st.markdown("""
<div class="footer">
    Accuracy Music © 2026
    <br>
    Projeto acadêmico de Ciência de Dados e Machine Learning
</div>
""", unsafe_allow_html=True)
