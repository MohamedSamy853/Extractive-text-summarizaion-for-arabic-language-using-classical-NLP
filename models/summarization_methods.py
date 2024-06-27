from sklearn.feature_extraction.text import TfidfVectorizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.reduction import ReductionSummarizer
from sumy.utils import get_stop_words
import numpy as np
import nltk
nltk.download("punkt")
def summary_with_tfidf(text , num_summary_sentence=3):
    sentences = nltk.tokenize.sent_tokenize(text)
    tfidfvectorizer = TfidfVectorizer()
    words_tfidf = tfidfvectorizer.fit_transform(sentences)
    #print(sentences)
    sent_sum = words_tfidf.sum(axis=1)
    extractive_sentence = np.argsort(sent_sum , axis=0)[::-1]
    
    text_summaries = []
    for i in range(0, len(sentences)):
        if i in extractive_sentence[:num_summary_sentence]:
            text_summaries.append(sentences[i])
    return "\n\n".join(text_summaries)
        
            
        
def summary_with_lsa(text , num_summary_sentence=3):
    language = 'arabic'
    stemmer = Stemmer(language)
    tokenizer = Tokenizer(language)

    parser = PlaintextParser.from_string(text , tokenizer)
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    
    text_summary = []
    
    for extractive_sentence in summarizer(parser.document , sentences_count=num_summary_sentence):
        text_summary.append(str(extractive_sentence))
        
    
    return "\n\n".join(text_summary)
        
def summary_with_text_rank(text , num_summary_sentence=3):
    language = 'arabic'
    stemmer = Stemmer(language)
    tokenizer = Tokenizer(language)
    parser = PlaintextParser.from_string(text , tokenizer)
    summarizer = TextRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    
    text_summary = []
    
    for extractive_sentence in summarizer(parser.document , sentences_count=num_summary_sentence):
        text_summary.append(str(extractive_sentence))
        
    return "\n\n".join(text_summary)
        
def summary_with_text_reduction(text , num_summary_sentence=3):
    language = 'arabic'
    stemmer = Stemmer(language)
    tokenizer = Tokenizer(language)
    parser = PlaintextParser.from_string(text , tokenizer)
    summarizer = ReductionSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    
    text_summary = []
        
    for extractive_sentence in summarizer(parser.document , sentences_count=num_summary_sentence):
        text_summary.append(str(extractive_sentence))
            
    return "\n\n".join(text_summary)

import gradio
import sklearn
import sumy
import numpy
import nltk
print(gradio.__version__)
print(sklearn.__version__)
print(sumy.__version__)
print(numpy.__version__)
print(nltk.__version__)