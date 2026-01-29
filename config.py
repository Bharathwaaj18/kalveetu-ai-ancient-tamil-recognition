import torch

class Config:
    DB_PATH = "data/predictions.sqlite"
    MODEL_PATH = "models/tamil_model_weights.pth"
    TEST_DIR = "data/test"
    IMG_SIZE = (64, 64)
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    CUSTOM_CSS = """
    <style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #111;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #ffffff;
        padding: 1.4rem;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
    }
    .prediction {
        font-size: 2.2rem;
        font-weight: 800;
    }
    .confidence {
        font-size: 1rem;
        color: #374151;
    }
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 0.9rem;
        margin-top: 2.5rem;
    }
    </style>
    """
