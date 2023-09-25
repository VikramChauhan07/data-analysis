import nltk
import os
import glob
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import re

# Define functions for text analysis
def clean_text(text):
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    clean_tokens = [word.lower() for word in tokens if word.lower() not in stop_words and re.match(r'\w', word)]
    return clean_tokens

def calculate_scores(clean_tokens, positive_words, negative_words):
    positive_score = sum(1 for word in clean_tokens if word in positive_words)
    negative_score = sum(1 for word in clean_tokens if word in negative_words)
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(clean_tokens) + 0.000001)
    return positive_score, negative_score, polarity_score, subjectivity_score

def calculate_readability(text):
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    words = clean_text(text)
    num_words = len(words)
    num_complex_words = sum(1 for word in words if len(word) > 2)
    avg_sentence_length = num_words / num_sentences
    percentage_complex_words = (num_complex_words / num_words) * 100
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_words_per_sentence = num_words / num_sentences
    return avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence

def calculate_complex_word_count(text):
    words = clean_text(text)
    complex_word_count = sum(1 for word in words if len(word) > 2)
    return complex_word_count

def calculate_syllable_per_word(text):
    words = clean_text(text)
    syllable_count = 0
    for word in words:
        vowels = "AEIOUaeiou"
        syllables = 0
        prev_char = None
        for char in word:
            if char in vowels:
                if prev_char is None or prev_char not in vowels:
                    syllables += 1
            prev_char = char
        if word.endswith(('es', 'ed')) and syllables > 1:
            syllables -= 1
        syllable_count += max(syllables, 1)
    return syllable_count / len(words)


def calculate_personal_pronouns(text):
    personal_pronoun_count = sum(1 for word in word_tokenize(text) if word.lower() in ["i", "we", "my", "ours", "us"])
    return personal_pronoun_count

def calculate_avg_word_length(text):
    words = clean_text(text)
    total_chars = sum(len(word) for word in words)
    avg_word_length = total_chars / len(words)
    return avg_word_length

# Specify the directory containing the text files
folder_path = "C:/Users/vikra/OneDrive/Desktop/New folder/output"

# Get a list of all text files in the folder
text_files = glob.glob(os.path.join(folder_path, "*.txt"))

# Initialize an empty list to store the results for each file
results_list = []

stop_words_folder = "C:/Users/vikra/OneDrive/Desktop/New folder/stopwords"

# Load stopwords from the folder
stop_words = set()
for filename in os.listdir(stop_words_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(stop_words_folder, filename), 'r') as stopword_file:
            stop_words.update(stopword_file.read().splitlines())

# Load stopwords and sentiment dictionaries

with open("C:/Users/vikra/OneDrive/Desktop/New folder/positive-words.txt", 'r') as positive_file:
    positive_words = set(positive_file.read().splitlines())

with open("C:/Users/vikra/OneDrive/Desktop/New folder/negative-words.txt", 'r') as negative_file:
    negative_words = set(negative_file.read().splitlines())


    
# Loop through each text file in the folder
for text_file in text_files:
    with open(text_file, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    
    # Calculate the variables for this text file
    positive_score, negative_score, polarity_score, subjectivity_score = calculate_scores(clean_text(text), positive_words, negative_words)
    avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence = calculate_readability(text)
    complex_word_count = calculate_complex_word_count(text)
    word_count = len(clean_text(text))
    syllable_per_word = calculate_syllable_per_word(text)
    personal_pronouns = calculate_personal_pronouns(text)
    avg_word_length = calculate_avg_word_length(text)

    # Store the results in a dictionary
    result_dict = {
        'File Name': os.path.basename(text_file),
        'POSITIVE SCORE': positive_score,
        'NEGATIVE SCORE': negative_score,
        'POLARITY SCORE': polarity_score,
        'SUBJECTIVITY SCORE': subjectivity_score,
        'AVG SENTENCE LENGTH': avg_sentence_length,
        'PERCENTAGE OF COMPLEX WORDS': percentage_complex_words,
        'FOG INDEX': fog_index,
        'AVG NUMBER OF WORDS PER SENTENCE': avg_words_per_sentence,
        'COMPLEX WORD COUNT': complex_word_count,
        'WORD COUNT': word_count,
        'SYLLABLE PER WORD': syllable_per_word,
        'PERSONAL PRONOUNS': personal_pronouns,
        'AVG WORD LENGTH': avg_word_length
    }

    # Append the results to the list
    results_list.append(result_dict)

# Create a DataFrame to store all the results
output_data = pd.DataFrame(results_list)

# Save the output to an Excel file
output_data.to_excel("C:/Users/vikra/OneDrive/Desktop/New folder/Output Data Structure.xlsx", index=False)

