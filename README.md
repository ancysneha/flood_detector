## 🌊 Flood Detection System (CNN + LSTM)


## Overview

This project detects flood-prone areas from images using a hybrid CNN + LSTM model. The CNN handles visual flood detection, while the LSTM incorporates temporal weather data (humidity, rainfall, etc.) to improve predictions.

The app is built with Streamlit for an interactive frontend and stores all predictions in a SQLite database for tracking and analysis.

## Features

Image Classification (CNN): Detects flood/no flood from uploaded images

Temporal Weather Integration (LSTM): Uses live weather data from OpenWeatherMap API

Prediction History: Saves predictions (filename, label, confidence, timestamp) in SQLite

Interactive Web App: Streamlit interface for uploading images and viewing results

Demo Ready: Run locally or access via Streamlit Cloud
