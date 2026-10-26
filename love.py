import streamlit as st
import time

st.set_page_config(
    page_title="هدية خاصة 🌙",
    page_icon="✨",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp { 
        background-color: #05070f; 
        color: #e2e8f0;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #1b263b, #0d1b2a);
        color: #f39c12;
        border: 2px solid #f39c12;
        border-radius: 25px;
        font-size: 18px;
        padding: 10px 24px;
        transition: 0.3s;
        box-shadow: 0 0 15px rgba(243, 156, 18, 0.3);
    }
    div.stButton > button:hover {
        background-color: #f39c12;
        color: #05070f;
        border-color: #f39c12;
        box-shadow: 0 0 25px rgba(243, 156, 18, 0.6);
    }

    .gold-title { 
        color: #f39c12; 
        text-align: center; 
        font-size: 2.2rem;
        font-weight: bold;
        text-shadow: 0 0 15px rgba(243, 156, 18, 0.5);
        margin-bottom: 25px;
    }

    .sub-title {
        color: #48cae4;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 0 0 10px rgba(72, 202, 228, 0.4);
    }

    .birth-date-box {
        text-align: center;
        background: linear-gradient(135deg, rgba(243, 156, 18, 0.15), rgba(255, 255, 255, 0.05));
        border: 1px solid #f39c12;
        padding: 10px 25px;
        border-radius: 50px;
        font-size: 1.3rem;
        font-weight: bold;
        color: #ffffff;
        letter-spacing: 2px;
        margin: 20px auto;
        width: fit-content;
        box-shadow: 0 0 15px rgba(243, 156, 18, 0.4);
    }

    .poem-box {
        text-align: center;
        font-family: 'Amiri', serif;
        font-size: 1.4rem;
        line-height: 2.2;
        color: #f8fafc;
        background: rgba(15, 23, 42, 0.65);
        padding: 25px;
        border-radius: 20px;
        border-right: 3px solid #f39c12;
        border-left: 3px solid #f39c12;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

if 'step1' not in st.session_state:
    st.session_state.step1 = False

st.markdown("<h1 class='gold-title'>✨ هل انت سنيوريتا؟ ✨</h1>", unsafe_allow_html=True)

if not st.session_state.step1:
    col1, col2 = st.columns(2)
    with col1:
        st.button("لا", use_container_width=True, disabled=True, key="disabled_no")
    with col2:
        if st.button("نعم 💖", use_container_width=True, key="enabled_yes"):
            st.session_state.step1 = True
            st.rerun()

if st.session_state.step1:
    st.balloons()
    st.snow()

    with st.spinner("جاري تحضير المفاجأة... 🌙"):
        time.sleep(1)

    st.markdown("<h3 class='sub-title'>💙 هاي الج ياحلا صدفة صارت 💙</h3>", unsafe_allow_html=True)

    st.markdown("### 🎵 الأغنية:")
    try:
        st.audio("محمد عبدالجبار - احلفك بالمحبه Muhammad Abdul-Jabbar - Ahlfak Belmahaba.mp3")
    except:
        st.warning("Audio file missing.")

    st.markdown("---")

    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        try:
            st.image(
                "download.jfif",
                use_container_width=True
            )
        except:
            st.error("Image file 'Download.jfif' missing.")

    st.markdown("<div class='birth-date-box'>✨ 2003 / 07 / 02 ✨</div>", unsafe_allow_html=True)

    st.markdown("""
        <div class='poem-box'>
            <div>يل جفك سما والنجم بي سهران</div>
            <div>الكمر اصبع تمنى يصير في جفك</div>
        </div>
    """, unsafe_allow_html=True)
