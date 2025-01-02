# Sentiment Analysis Web Application  

| Positive Sentiment         | Negative Sentiment         |
|----------------------------|----------------------------|
| ![Positive GIF](test%20results/positive%20test.gif) | ![Negative GIF](test%20results/negative%20test.gif) |

> A powerful sentiment analysis tool leveraging cutting-edge NLP models from Hugging Face, designed for real-time sentiment classification and visualization.

---

## 📖 Features  
- **Real-Time Sentiment Analysis**: Analyze text to classify as positive or negative.
- **Interactive Visualization**: View prediction confidence through bar charts.
- **API Support**: Provides REST API for external applications.

---

## 🛠️ Quick Start
### Install Dependencies
Run the following command to install all required libraries:
```bash
pip install -r requirements.txt
```
### Run Locally
Launch the Streamlit application:
```bash
streamlit run streamlit_app.py
```

## 🛠️ REST API Documentation

Test sentiment analysis via API:

- **Endpoint**: `/predict`
- **Method**: POST
- **Request Format**:
```json
{
  "text": "今天天气真好，让人心情舒畅"
}
```

## 🧰 Technology Stack

- **Frontend**: Streamlit
- **Backend**: PyTorch, Hugging Face Transformers
- **Visualization**: Matplotlib
- **API**: Flask

## 📊 Screenshots

### Main Interface
This is the main interface where users can input text for sentiment analysis:
![Main Interface](path-to-main-interface-image)

### Sentiment Distribution
Visualizes the confidence scores for sentiment prediction:
![Sentiment Distribution](path-to-sentiment-distribution-image)



