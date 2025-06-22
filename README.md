# 💧 Water Quality Prediction - Deployment

This is a machine learning web application built using **Flask** that predicts whether water is **safe for drinking** or not, based on key chemical properties. The model is trained on a publicly available dataset and deployed with a user-friendly interface to receive input and display predictions.

## 🚀 How It Works

- User enters water sample data (pH, Sulfate, Solids, etc.)
- Inputs are scaled using a saved `StandardScaler`
- A trained **Random Forest** model predicts potability
- Prediction result is displayed: **Safe** or **Not Safe**
- Users can submit feedback, which is saved in `feedback.csv`

## Requirements & Setup

### Requirements

All dependencies are listed in the `requirements.txt` file.

### 🛠️ Installation Steps

1. **Clone the repository**
   bash
   git clone https://github.com/Zubia-Ejaz/WaterQualityPrediction-Deployment.git
   cd WaterQualityPrediction-Deployment

2. **Install the required libraries**
   bash
   pip install -r requirements.txt


3. **Run the Flask app**
   bash
   python waterquality_app.py


4. **Open in browser**
## Project Structure

```
WaterQualityPrediction-Deployment/
├── model.pkl
├── scaler.pkl
├── feedback.csv
├── waterquality_app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/ (if any)
└── README.md
```