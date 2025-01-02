from flask import Flask, request, jsonify
from app.model import SentimentModel

# 初始化 Flask 应用和模型
app = Flask(__name__)
model = SentimentModel(model_path="app/saved_model")  # 指定模型路径

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Invalid input, 'text' key is required"}), 400

    text = data["text"]
    result = model.predict(text)
    return jsonify(result)
