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
---

### ✅ Task 1: Data Collection and Preprocessing

This task focuses on extracting Amharic e-commerce data from Telegram channels and preparing it for Named Entity Recognition (NER) modeling.

#### 🔹 Telegram Scraper
- Implemented using the `Telethon` library.
- Connects to the Telegram API using credentials stored securely in a `.env` file.
- Joins and fetches messages from public e-commerce Telegram channels.
- Stores messages in structured `.json` and `.csv` formats inside the `data/raw/` directory.

#### 🔹 Session Management
- Session files (`.session`) are securely stored and excluded from version control via `.gitignore`.
- Ensures the bot doesn't require re-authentication every run.

#### 🔹 Data Cleaning & Preprocessing
- Raw messages often contain emojis, links, timestamps, and multimedia indicators.
- Cleaning pipeline includes:
  - Removing emojis and non-text characters
  - Standardizing Amharic punctuation
  - Tokenizing and lowercasing
- Cleaned outputs are saved to `data/processed/telegram_messages_cleaned.csv`.

#### 🔹 Scripts
- `scripts/telegram_scraper.py`: Connects to Telegram and extracts raw message data.
- `scripts/data_preprocessor.py`: Cleans and structures raw messages into a training-ready format.

---

### ✅ Task 2: Manual Entity Labeling in CoNLL Format

This task involves labeling a subset of the Amharic dataset manually for NER training using the CoNLL format.

#### 🔹 Objective
- Identify and tag important entities in Amharic Telegram messages:
  - `PRODUCT`, `PRICE`, and `LOCATION`.

#### 🔹 Format: CoNLL (Column-Based)
- Each line contains a word and its corresponding tag.
- Messages are separated by blank lines.

#### 🔹 BIO Tagging Schema Used
| Tag         | Description                                   |
|-------------|-----------------------------------------------|
| B-PRODUCT   | Beginning of a product name                   |
| I-PRODUCT   | Inside a product name                         |
| B-LOC       | Beginning of a location name                  |
| I-LOC       | Inside a location name                        |
| B-PRICE     | Beginning of a price mention                  |
| I-PRICE     | Inside a price mention                        |
| O           | Outside any entity                            |

#### 🔹 Example (Sample CoNLL Output)
ለልጆች B-PRODUCT
ጫማ I-PRODUCT
በ O
350 B-PRICE
ብር I-PRICE

በአዲስ B-LOC
አበባ I-LOC


#### 🔹 Workflow
- 50 messages sampled from `telegram_messages_cleaned.csv`.
- Tokens labeled manually by reviewing each sentence.
- Saved as `data/labeled/amharic_ner.conll`.

#### 🔹 Scripts & Notebook
- `notebooks/3_data_labeling.ipynb`: Includes sample selection, token display, and export function for CoNLL.
- `save_conll()` function used to store labeled data in the correct format.

---



## Acknowledgments
Hugging Face for transformer models

Telegram API developers

Ethiopian NLP research community
## Contact
Shegaw Adugna  
Project Link: https://github.com/Shegaw-21hub/EthioMart-NER