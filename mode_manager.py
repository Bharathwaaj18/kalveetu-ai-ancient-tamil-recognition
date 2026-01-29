import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

from config import Config
from model import TamilLetterCNN

class ModelManager:
    def __init__(self, model_path, class_names, device):
        self.class_names = class_names
        self.device = device
        self.model = self._load_model(model_path)
        self.transform = transforms.Compose([
            transforms.Resize(Config.IMG_SIZE),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5],
                                 [0.5, 0.5, 0.5])
        ])

    def _load_model(self, model_path):
        model = TamilLetterCNN(len(self.class_names)).to(self.device)
        state_dict = torch.load(model_path, map_location=self.device)
        model.load_state_dict(state_dict)
        model.eval()
        return model

    def predict(self, image: Image.Image):
        image = image.convert("RGB")
        tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            logits = self.model(tensor)
            probs = F.softmax(logits, dim=1)
            idx = probs.argmax(dim=1).item()
            confidence = probs[0, idx].item()

        return self.class_names[idx], confidence
