## 🌊 Flood Detection System (CNN + LSTM)


## Overview

This project detects flood-prone areas from images using a hybrid CNN + LSTM model. The CNN handles visual flood detection, while the LSTM incorporates temporal weather data (humidity, rainfall, etc.) to improve predictions.

The app is built with Streamlit for an interactive frontend and stores all predictions in a SQLite database for tracking and analysis.

## Features

->Image Classification (CNN): Detects flood/no flood from uploaded images

->Temporal Weather Integration (LSTM): Uses live weather data from OpenWeatherMap API

->Prediction History: Saves predictions (filename, label, confidence, timestamp) in SQLite

->Interactive Web App: Streamlit interface for uploading images and viewing results

->Demo Ready: Run locally or access via Streamlit Cloud

## Project Structure
flood_detector/
├── app.py              # Streamlit app (frontend + model inference + DB logging)
├── cnn_model.py        # CNN model for flood detection
├── lstm_model.py       # LSTM model for temporal weather input
├── weather_api.py      # Fetches live weather data (API key hidden via secrets)
├── predict.py          # Script for standalone CNN inference
├── run.py              # Alternative Streamlit demo (pickle-based)
├── train_cnn.py        # Train standalone CNN (ResNet50) on dataset
├── train_model.py      # Train combined CNN + LSTM model
├── model.pth           # Trained combined model weights
├── flood_logs.db       # SQLite database (auto-created)
├── dataset/            # Flood/Non-Flood images
│   ├── flooded/
│   └── non_flooded/
├── requirements.txt
└── README.md

## Dataset
Structure:

dataset/
├── flooded/       # Images of flooded areas
└── non_flooded/   # Images of safe/non-flooded areas

Usage: train_cnn.py or train_model.py scripts automatically read this folder structure.

## INSTALLATION
1.Clone the repository:

git clone https://github.com/ancysneha/flood_detector.git
cd flood_detector

2.Install dependencies:
pip install -r requirements.txt

3.Add your OpenWeatherMap API key:

For local development, you can directly add it in weather_api.py:

API_KEY = "<YOUR_API_KEY>"


For production, use Streamlit Secrets or .env files to hide keys.

## TRAINING
CNN-only Model (ResNet50)
python train_cnn.py

->Uses ResNet50 pretrained on ImageNet
->Trains for 10 epochs (can adjust in code)
->Saves weights as model.pth

## Combined CNN + LSTM Model
python train_model.py

->Uses custom FloodCNN + LSTMForecast
->LSTM input sequence generated from dataset (or live weather)
->Saves trained weights as model.pth

## Running the app
streamlit run app.py

- Upload an image (jpg/jpeg/png)
- See live weather data for Coimbatore
- Get Flood / No Flood prediction with confidence score
- Optional: View prediction history stored in flood_logs.db

## API & Security:

Weather API: OpenWeatherMap
## API Key Handling:
Local development: can be hardcoded in weather_api.py temporarily
Production: store in Streamlit secrets or environment variables to avoid exposing your key

## TECHNOLOGY STACK:
| Component      | Technology                      |
| -------------- | ------------------------------- |
| Frontend       | Streamlit                       |
| Deep Learning  | PyTorch (CNN + LSTM)            |
| Image Handling | PIL, torchvision                |
| Database       | SQLite                          |
| Weather API    | OpenWeatherMap API              |
| Training       | torch.utils.data.DataLoader     |
| Models         | ResNet50 (CNN), FloodCNN + LSTM |

## Database:

File: flood_logs.db
Table: logs
Columns: id, filename, prediction, confidence, timestamp
Created automatically on first run

## How It Works

CNN extracts features from uploaded image
LSTM takes in a 10-step weather sequence (humidity or rainfall as scalar input)
Outputs from CNN and LSTM are combined to produce final logits
Softmax used to calculate probabilities
Predicted label and confidence stored in SQLite database
Streamlit app displays prediction, confidence, and logs

## Live Demo:
https://flooddetector-kfayfeobn6epmvvy3fndz4.streamlit.app/

## Author:

Ancy Sneha — GitHub Profile
