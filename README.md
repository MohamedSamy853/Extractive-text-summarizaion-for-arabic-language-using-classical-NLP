# Extractive Text Summarization for Arabic Language using Classical NLP
In this project, I developed and compared different methods for text summarization of Arabic articles. Utilizing  extractive techniques, I explored various algorithms such LSA , text rank , tfidf , text reduction and approaches to generate concise and accurate summaries, enhancing the accessibility and comprehension of Arabic textual content

## Overview
This project focuses on implementing extractive text summarization techniques for the Arabic language using classical Natural Language Processing (NLP) methods. The goal is to create a system that can generate concise summaries from Arabic text inputs.

## Project Stages

### 1. Data Preprocessing
In the initial stage, the data undergoes rigorous cleaning and preprocessing:
- Removal of emails, phone numbers, URLs, and short URLs.
- Filtering out non-Arabic words, emojis, and other non-relevant characters.

### 2. Modeling
Several NLP models and techniques are applied to the preprocessed data:
- TF-IDF (Term Frequency-Inverse Document Frequency)
- LSA (Latent Semantic Analysis)
- TextRank algorithm
- Text Reduction techniques

### 3. Evaluation
Each model's performance is evaluated using BLEU (Bilingual Evaluation Understudy) score:
- Evaluation reveals that the Text Reduction technique performs the best, despite its limitation in semantic understanding.

### 4. Deployment
The summarization model is deployed in two main environments:
- Integration into a radio application for real-time use.
- Deployment on Hugging Face Spaces for broader accessibility.

## Demo
For a demonstration of the deployed model, visit the [demo on Hugging Face Spaces](https://huggingface.co/spaces/Mohamed-Sami/extractive-text-summarization).

## Usage
To use the model:
1. Clone the repository.
2. Install the necessary dependencies.
3. Follow the instructions in the repository to integrate the model into your application.

