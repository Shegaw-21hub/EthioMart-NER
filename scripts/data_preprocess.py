# data_preprocess.py

import os
import re
import json
import pandas as pd
import emoji
from nltk.tokenize import word_tokenize
import nltk

# Download tokenizer model if not present
nltk.download('punkt', quiet=True)


def clean_amharic_text(text: str) -> str:
    """
    Clean Amharic text by:
    - Removing URLs
    - Removing emojis
    - Removing long dot sequences
    - Keeping Amharic Unicode, basic punctuation, letters, and numbers
    - Normalizing whitespace
    """
    if not isinstance(text, str):
        return ""

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove emojis
    text = emoji.replace_emoji(text, replace='')

    # Remove long sequences of dots (e.g. .........)
    text = re.sub(r'\.{3,}', ' ', text)

    # Keep Amharic Unicode range (1200-137F), basic punctuation, letters, numbers
    text = re.sub(r'[^\w\s\u1200-\u137F.,!?]', '', text)

    # Normalize whitespace
    text = ' '.join(text.split())

    return text.strip()


def load_data(input_path: str) -> pd.DataFrame:
    """
    Load data from JSON or CSV file into a pandas DataFrame.
    Raises an error for unsupported formats or missing 'text' column.
    """
    ext = os.path.splitext(input_path)[-1].lower()

    if ext == ".json":
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
    elif ext == ".csv":
        df = pd.read_csv(input_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    if "text" not in df.columns:
        raise KeyError("'text' column not found in input file.")

    return df


def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and tokenize the 'text' column of a DataFrame.
    Drops rows where cleaned text is empty.
    """
    df["cleaned_text"] = df["text"].apply(clean_amharic_text)
    df["tokens"] = df["cleaned_text"].apply(word_tokenize)

    # Drop empty cleaned_text rows
    df = df[df["cleaned_text"].str.strip() != ""]

    return df


def save_processed_data(df: pd.DataFrame, output_dir: str, input_filename: str) -> str:
    """
    Save processed DataFrame to a CSV file in output_dir with a cleaned suffix.
    Returns the path of the saved file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = os.path.splitext(os.path.basename(input_filename))[0]
    output_path = os.path.join(output_dir, f"{base_name}_cleaned.csv")

    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    return output_path


def main(input_path: str, output_dir: str = "../data/processed") -> None:
    """
    Load, clean, tokenize, and save data.
    """
    print(f"Loading data from: {input_path}")
    df = load_data(input_path)

    print("Cleaning and tokenizing data...")
    df_processed = preprocess_dataframe(df)

    print(f"Saving processed data to directory: {output_dir}")
    saved_path = save_processed_data(df_processed, output_dir, input_path)

    print(f"✅ Processed file saved at: {saved_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Clean and tokenize Amharic Telegram messages")
    parser.add_argument("input_path", help="Path to input JSON or CSV file")
    parser.add_argument("--output_dir", default="../data/processed", help="Directory to save cleaned CSV")

    args = parser.parse_args()
    main(args.input_path, args.output_dir)
