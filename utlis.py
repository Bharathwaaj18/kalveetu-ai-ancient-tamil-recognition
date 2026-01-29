import os
import streamlit as st
from config import Config

@st.cache_data
def load_class_names():
    if not os.path.exists(Config.TEST_DIR):
        return []
    return sorted(
        d for d in os.listdir(Config.TEST_DIR)
        if os.path.isdir(os.path.join(Config.TEST_DIR, d))
    )
