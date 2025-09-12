# EthioMart: Amharic Named Entity Recognition for Telegram E-Commerce
![EthioMart Banner](https://via.placeholder.com/1200x400?text=EthioMart+NER+System)
## 📌 Project Overview

EthioMart transforms Ethiopia's decentralized Telegram e-commerce into a unified marketplace by extracting business entities (products, prices, locations) from Amharic messages. This end-to-end solution features:

- **Automated data pipeline** from Telegram channels
- **Custom Amharic NER dataset** with 50 labeled messages
- **State-of-the-art multilingual models** fine-tuned for Amharic
- **Vendor analytics engine** for micro-lending decisions
## 🏆 Key Achievements

✅ **Data Pipeline**  
- Collected 1,000+ messages from 5 Telegram channels  
- Developed preprocessing for Amharic text normalization  

✅ **NER Implementation**  
- Manually labeled 50 messages (600+ tokens) in CoNLL format  
- Fine-tuned 3 transformer models (F1 scores 0.83-0.88)  

✅ **Advanced Features**  
- Model interpretability with SHAP/LIME  
- Vendor scoring system for lending decisions  
## 📂 Repository Structure

```
EthioMart-NER/
├── data/
│   ├── raw/                  # JSON/CSV from Telegram
│   ├── processed/            # Cleaned messages
│   └── labeled/              # amharic_ner.conll
│
├── models/
│   ├── xlm-roberta/          # Best model (F1=0.88)
│   ├── distilbert/           # Fastest model
│   └── mbert/                # Balanced option
│
├── notebooks/
│   ├── 1_data_collection.ipynb
│   ├── 2_data_preprocessing.ipynb
│   ├── 3_data_labeling.ipynb      # CoNLL creation
│   ├── 4_model_training.ipynb     # Fine-tuning
│   ├── 5_model_comparison.ipynb   # Benchmarking
│   ├── 6_model_interpretability.ipynb
│   └── 7_vendor_scorecard.ipynb
│
├── scripts/
│   ├── telegram_scraper.py       # Data collection
│   ├── data_preprocessor.py      # Cleaning pipeline
│   └── vendor_analyzer.py        # Lending scores
│
├── .env.example                 # API configuration
├── requirements.txt             # Dependencies
└── EthioMart_NER_Report.pdf     # 15-page final report
```
```markdown
## 🛠️ Installation Guide

### Prerequisites
- Python 3.8+
- PowerShell (Windows)
- NVIDIA GPU (recommended)

### Setup
```powershell
# Clone repository
git clone https://github.com/Shegaw-21hub/EthioMart-NER.git
cd EthioMart-NER

# Create virtual environment
python -m venv ethiomart-venv
.\ethiomart-venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up Telegram API (get credentials from https://my.telegram.org)
copy .env.example .env
```

```markdown
## 🚀 Usage Instructions

### 1. Data Collection
````
```powershell
python scripts/telegram_scraper.py
```

### Channels Scraped:

Shageronlinestore

AddisMercato

EthioDeal

ShegerShop

AddisShop
## 2. Data Preprocessing
```
python scripts/data_preprocessor.py data/raw/telegram_messages_*.json
```
### Cleaning Steps:

Removes emojis, URLs, special characters

Tokenizes Amharic-English mixed text

Outputs to data/processed/

```markdown
## 📊 Model Performance

| Model          | Precision | Recall | F1-Score | Speed (ms/sample) | RAM Usage |
|----------------|-----------|--------|----------|-------------------|-----------|
| XLM-Roberta    | 0.89      | 0.87   | 0.88     | 120               | 4.2GB     |
| mBERT          | 0.86      | 0.85   | 0.85     | 150               | 3.8GB     |
| DistilBERT     | 0.84      | 0.82   | 0.83     | 80                | 2.1GB     |

**Best Model Selected:**  
`models/xlm-roberta/final` (Highest F1-score)
```
## 🔍 Model Interpretability

### SHAP Analysis Example
![SHAP Visualization](https://via.placeholder.com/600x300?text=SHAP+Values+for+Amharic+NER)

Key Findings:
- Price detection relies heavily on numeric tokens
- Product names require contextual understanding
- Location entities often follow prepositions
## 💼 Vendor Scorecard System

**Metrics Calculated:**
1. **Activity Score** (Posts/week)
2. **Engagement Score** (Avg. views/post)  
3. **Price Profile** (Avg. product price)  

**Lending Score Formula:**  
`0.5*(Normalized Views) + 0.3*(Post Frequency) + 0.2*(Price Stability)`

**Sample Output:**
| Vendor          | Avg. Views | Posts/Week | Avg. Price | Score |
|-----------------|------------|------------|------------|-------|
| ShagerOnline    | 1,200      | 14         | 450 ETB    | 0.87  |
| AddisMercato    | 950        | 9          | 680 ETB    | 0.72  |


```markdown
## 🙌 Acknowledgments

- **Hugging Face** for transformer models and datasets library
- **Telegram API** for accessible e-commerce data
- **Addis Ababa University** for Amharic NLP research
- **PyTorch** for GPU-accelerated training
```
## 📬 Contact

**Shegaw Adugna**   

*© 2023 EthioMart NER Project - MIT License*
