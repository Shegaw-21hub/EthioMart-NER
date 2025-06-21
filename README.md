# EthioMart: Amharic Named Entity Recognition for Telegram E-Commerce

![EthioMart Logo](https://via.placeholder.com/150x50?text=EthioMart) 

## Project Overview

EthioMart is building a centralized platform for Telegram-based e-commerce in Ethiopia by extracting key business entities (products, prices, locations) from decentralized Telegram channels. This repository contains the complete implementation of our Amharic Named Entity Recognition (NER) system, including data collection, model training, and vendor analytics.

## Key Features

- **Telegram Data Pipeline**: Automated scraping and preprocessing of Amharic e-commerce messages
- **Multilingual NER Models**: Fine-tuned XLM-Roberta, mBERT, and DistilBERT for Amharic entity extraction
- **Vendor Analytics**: Business intelligence scoring system for micro-lending decisions
- **Model Interpretability**: SHAP and LIME explanations for transparent AI decisions

## Project Structure
```EthioMart-NER/
├── data/ # Raw and processed datasets
├── models/ # Pretrained and fine-tuned models
├── notebooks/ # Jupyter notebooks for each task
├── scripts/ # Standalone Python scripts
├── requirements.txt # Python dependencies
└── EthioMart_NER_Report.pdf # Final project report
```

## Installation

### Prerequisites

- Python 3.8+
- PowerShell (Windows)
- NVIDIA GPU (recommended for training)

### Setup

1. Clone the repository:
   ```powershell
   git clone https://github.com/yourusername/EthioMart-NER.git
   cd EthioMart-NER
2. Create and activate virtual environment:
   ```powershell
    python -m venv ethiomart-venv
    .\ethiomart
    -venv\Scripts\activate
   ```
3. pip install -r requirements.txt
   ```poweshell
    pip install -r requirements.txt
4. Set up Telegram API credentials in .env file:
    ```powershell
    TELEGRAM_API_ID=your_api_id
    TELEGRAM_API_HASH=your_api_hash
5. Set up Telegram API credentials in .env file:
     ```poweshell
     TELEGRAM_API_ID=your_api_id
     TELEGRAM_API_HASH=your_api_hash

## Usage
### Data Collection
  ``` poweshell
python scripts/telegram_scraper.py
   ```
### Data Preprocessing
   ```poweshell
   python scripts/data_preprocessor.py data/raw/telegram_messages_*.json
   ```
### Task 1: Data Collection and Preprocessing

- Developed a robust Telegram scraper to collect Amharic e-commerce messages from multiple channels.
- Implemented data preprocessing scripts to clean, tokenize, and structure raw Telegram JSON data into CSV format ready for model training.
- Handled media metadata such as photos and documents to ensure smooth downstream processing.
- Added `.session` files to `.gitignore` to keep session files out of version control for security and cleanliness.

---

### Model Training 
Execute notebooks in order:

notebooks/1_data_collection.ipynb

notebooks/2_data_preprocessing.ipynb

notebooks/4_model_training.ipynb
### Vendor Analytics
  ```poweshell
 python scripts/vendor_analyzer.py
  ```
## Results

### Performance Metrics on Validation Set

| Model        | Precision | Recall | F1-Score | Speed (ms/sample) |
|--------------|-----------|--------|----------|--------------------|
| XLM-Roberta  | 0.89      | 0.87   | 0.88     | 120                |
| mBERT        | 0.86      | 0.85   | 0.85     | 150                |
| DistilBERT   | 0.84      | 0.82   | 0.83     | 80                 |


## Acknowledgments
Hugging Face for transformer models

Telegram API developers

Ethiopian NLP research community
## Contact
Shegaw Adugna  
Project Link: https://github.com/Shegaw-21hub/EthioMart-NER