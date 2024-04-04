import pandas as pd
from transformers import pipeline
from multiprocessing import Pool, cpu_count
from nltk.tokenize import word_tokenize
emotion_pipeline = pipeline('sentiment-analysis', model="arpanghoshal/EmoRoBERTa")
def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
def process_batch(texts):
    print("Processing batch...")
    batch_results = emotion_pipeline(texts)
    emotion_labels = [result['label'] for result in batch_results]
    return emotion_labels
def main():
    file_path = 'ssss.csv'
    df = load_dataset(file_path)
    if df is None:
        return
    text_column = 'sentence_spacy'
    chunk_size = 50000  
    batch_size = 256  
    emotional_labels = []
    num_chunks = len(df) // chunk_size + (len(df) % chunk_size > 0)

    for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
        print(f"Processing chunk {i+1}/{num_chunks}...")
        texts = chunk[text_column].tolist()
        # Split texts into batches
        for j in range(0, len(texts), batch_size):
            print(f"Processing batch {j//batch_size+1}...")
            batch_texts = texts[j:j + batch_size]
            batch_results = process_batch(batch_texts)
            emotional_labels.extend(batch_results)
    df['emotion_label'] = emotional_labels

    output_path = 'final.csv'
    df.to_csv(output_path, index=False)
    print("Emotional analysis completed and dataset updated successfully.")

if __name__ == "__main__":
    main()
