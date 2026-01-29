import streamlit as st
from PIL import Image

from config import Config
from utils import load_class_names
from model_manager import ModelManager
from database import DatabaseManager

@st.cache_resource
def init_app():
    class_names = load_class_names()
    model_manager = ModelManager(
        Config.MODEL_PATH,
        class_names,
        Config.DEVICE
    )
    db_manager = DatabaseManager(Config.DB_PATH)
    return model_manager, db_manager


def main():
    st.set_page_config("Kalveetu AI", "📜", layout="centered")
    st.markdown(Config.CUSTOM_CSS, unsafe_allow_html=True)

    model_manager, db_manager = init_app()

    st.markdown('<div class="main-title">📜 Kalveetu AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Ancient Tamil Character Recognition</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload character image", ["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, width=400)

        if st.button("🔍 Predict", use_container_width=True):
            prediction, confidence = model_manager.predict(image)
            db_manager.log_prediction(uploaded_file.name, prediction, confidence)

            st.markdown(f"""
            <div class="card">
                <div class="prediction">{prediction}</div>
                <div class="confidence">Confidence: {confidence:.2%}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="footer">Final Year Project • Kalveetu AI</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
