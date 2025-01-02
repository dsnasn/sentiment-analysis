import streamlit as st
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# 页面设置
st.set_page_config(page_title="Sentiment Analysis Tool - 情感分析工具", page_icon="📊", layout="wide")

# 加载模型类
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
            return sentiment, confidence, probabilities[0].tolist()

# 缓存模型加载
@st.cache_resource
def load_model():
    return SentimentModel(model_path="app/saved_model")

model = load_model()

# 标题
st.title("📊 Sentiment Analysis Tool - 情感分析工具")
st.markdown("""
This is a sentiment analysis tool based on NLP models, capable of analyzing text sentiment (positive or negative).  
这是一个基于 NLP 模型的情感分析工具，可以分析文本情感（正向或负向）。
- 🔍 Input any text to check the sentiment classification and model confidence.  
  输入任意文本，查看情感分类和模型置信度。
- 📡 API support is provided for external calls.  
  提供 API 服务，支持外部调用。
""")

# **左侧栏**
with st.sidebar:
    st.header("📘 Instructions - 使用说明")
    st.markdown("""
    1. Enter a piece of text for sentiment analysis.  
       输入一段文本进行情感分析。
    2. View the classification result and confidence score.  
       查看分类结果和置信度。
    3. Test REST API using tools like Postman.  
       测试 REST API，通过 Postman 等工具发送请求。
    """)
    st.info("Model Source: Hugging Face Transformers\n技术栈：Streamlit + PyTorch")

# **主内容**
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Enter Text - 输入文本")
    user_input = st.text_area("Enter text for analysis (请输入待分析的文本):", "")

    if st.button("Analyze Sentiment - 分析情感"):
        if user_input.strip():
            # 调用模型进行预测
            sentiment, confidence, probabilities = model.predict(user_input)
            sentiment_label = "Positive 😊 - 正向" if sentiment == 1 else "Negative 😞 - 负向"

            # 显示结果
            st.success(f"**Sentiment Category - 情感类别**: {sentiment_label}")
            st.info(f"**Confidence Score - 置信度**: {confidence:.2f}")

            # 可视化分布图
            st.subheader("Sentiment Distribution")
            labels = ["Negative", "Positive"]
            fig, ax = plt.subplots()
            ax.bar(labels, probabilities, color=["red", "green"])
            ax.set_ylabel("Confidence")
            ax.set_title("Sentiment Prediction Distribution")
            st.pyplot(fig)
        else:
            st.warning("Please enter valid text! - 请输入有效文本！")

with col2:
    st.subheader("📊 Example Inputs - 示例输入")
    st.markdown("""
    - **Positive Sentiment - 正向情感**:  
      今天真是美好的一天！
    - **Negative Sentiment - 负向情感**:  
      服务态度太差了，真的很失望。
    """)

# API 文档部分
st.markdown("---")
st.header("📡 API Documentation - API 文档")
st.markdown("""
Test sentiment analysis through REST API:  
通过 REST API 测试情感分析：
- **Endpoint**: `/predict`
- **Method - 方法**: POST
- **Request Format - 请求格式**: JSON, e.g. / 示例：  
```json
{
  "text": "今天心情很好！"
}
""")