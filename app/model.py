import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 定义模型类
class SentimentModel:
    def __init__(self, model_path="app/saved_model"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path).to(self.device)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512).to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
            probabilities = torch.nn.functional.softmax(outputs.logits, dim=1)
            sentiment = torch.argmax(probabilities).item()
            confidence = probabilities[0][sentiment].item()
        sentiment_label = "positive" if sentiment == 1 else "negative"
        return {"sentiment": sentiment_label, "confidence": confidence}
