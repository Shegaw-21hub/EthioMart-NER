# EthioMart: Amharic Named Entity Recognition for Telegram E-Commerce

![EthioMart Logo](https://via.placeholder.com/150x50?text=EthioMart)

## 📌 Project Overview

EthioMart aims to centralize Ethiopia's decentralized Telegram-based e-commerce ecosystem. We extract meaningful business entities such as products, prices, and locations from raw Amharic messages using Named Entity Recognition (NER). This repository contains all components of the data pipeline: collection, preprocessing, annotation, and model preparation.

---

## 🚀 Key Features

- **Telegram Data Pipeline**: End-to-end automation for message scraping and data preprocessing.
- **NER-Ready Dataset**: Manual labeling of Amharic data in standard CoNLL format.
- **Multilingual NER Models**: Fine-tuned XLM-Roberta, mBERT, and DistilBERT for low-resource Amharic extraction.
- **Vendor Analytics (Planned)**: Convert extracted information into actionable lending insights.
- **Model Interpretability**: Tools like SHAP and LIME to ensure explainable AI.

---

## 📁 Project Structure

```text
EthioMart-NER/
├── data/                # Raw, cleaned, and labeled datasets
├── models/              # Pretrained and fine-tuned NER models
├── notebooks/           # Jupyter notebooks for each pipeline stage
├── scripts/             # Data collection and processing scripts
├── requirements.txt     # Python dependencies
└── EthioMart_NER_Report.pdf  # Final project report
```
## ⚙️ Installation
## ✅ Prerequisites
Python 3.8+

PowerShell (Windows)

NVIDIA GPU (recommended for training)
## 🔧 Setup Instructions
### 1. lone the Repository
   ```
   git clone https://github.com/yourusername/EthioMart-NER.git
cd EthioMart-NER
```
### 2. Create and Activate Virtual Environment
   ```
   python -m venv ethiomart-venv
  .\ethiomart-venv\Scripts\activate
   ```
### pip install -r requirements.txt
 ```pip install -r requirements.txt
```
### 4. Set Up Telegram API Credentials
Create a .env file in the root directory:
 ```
 TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
```
## 🧪 Usage Instructions
```
python scripts/telegram_scraper.py
```
## 🧹 Data Preprocessing
```
python scripts/data_preprocessor.py data/raw/telegram_messages_*.json
```
## ✅ Task 1: Data Collection and Preprocessing

### 🔹 Telegram Scraper
- Built using the `Telethon` library.
- Scrapes messages from public Telegram e-commerce channels.
- Authenticates via `.env` API credentials.
- Outputs stored in `.json` and `.csv` formats under `data/raw/`.

### 🔹 Session File Management
- `.session` files are excluded via `.gitignore` to avoid sharing sensitive authentication state.

## 🔹 Data Cleaning

- Cleans raw Telegram messages by removing:
  - Emojis
  - Decorative symbols
  - URLs and links
  - Repetitive punctuation (e.g., `.....`)
  - Non-textual clutter
- Standardizes whitespace and filters meaningful content.
- Tokenizes mixed Amharic-English text using `nltk.word_tokenize`.
- **Output saved to:**  
  `data/processed/telegram_messages_20250621_052911_cleaned.csv`

---

## 🔹 Scripts

- `telegram_scraper.py`:  
  Scrapes Telegram channels and exports messages in `.json` or `.csv`.

- `data_preprocess.py`:  
  Cleans and tokenizes raw messages for downstream NLP tasks like NER.  
  Can be used both **programmatically** or via the **command line**.

### 🎯 Objective
Label a subset of Amharic messages (30–50) for NER training using the CoNLL format and BIO tagging scheme.

### 🏷️ Entity Tags

| Tag        | Description                        |
|------------|------------------------------------|
| B-PRODUCT  | Beginning of a product entity      |
| I-PRODUCT  | Inside a product entity            |
| B-LOC      | Beginning of a location entity     |
| I-LOC      | Inside a location entity           |
| B-PRICE    | Beginning of a price entity        |
| I-PRICE    | Inside a price entity              |
| O          | Outside any named entity           |

### 📝 Format Example
ለልጆች B-PRODUCT

ጫማ I-PRODUCT

በ O

350 B-PRICE

ብር I-PRICE

በአዲስ B-LOC

አበባ I-LOC

### ⚙️ Workflow
- 50 messages sampled from the cleaned dataset.
- Tokens manually labeled using the BIO format.
- Saved as:  
  `data/labeled/amharic_ner.conll`

### 🧾 Related Notebook
- `notebooks/3_data_labeling.ipynb`: Includes token visualization, annotation guidance, and `.conll` export logic via `save_conll()` function.
## 📊 Results Snapshot *(Coming Soon)*

| Model        | Precision | Recall | F1-Score | Speed (ms/sample) |
|--------------|-----------|--------|----------|--------------------|
| XLM-Roberta  | 0.89      | 0.87   | 0.88     | 120                |
| mBERT        | 0.86      | 0.85   | 0.85     | 150                |
| DistilBERT   | 0.84      | 0.82   | 0.83     | 80                 |

---

## 🙏 Acknowledgments

- 🤗 **Hugging Face** – for multilingual transformer models  
- 📡 **Telegram API** – for accessible channel-based commerce data  
- 🇪🇹 **Ethiopian NLP research community** – for inspiring low-resource NER work

---

## 📬 Contact

**Shegaw Adugna**  
GitHub: [https://github.com/Shegaw-21hub/EthioMart-NER](https://github.com/Shegaw-21hub/EthioMart-NER)
