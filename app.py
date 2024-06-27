from models.summarization_methods import summary_with_lsa
from models.summarization_methods import summary_with_text_rank
from models.summarization_methods import summary_with_text_reduction
from models.summarization_methods import summary_with_tfidf
from utils.perprocess import clean_text
import gradio as gr
from enum import Enum

class SummarizationMehods(Enum):
    LSA = 0
    TextRank = 1
    TextReduction = 2 
    TfIdf = 3


def summary(text , num_sentences=3 , method = SummarizationMehods(0).name):
    text = clean_text(text)
    if method.casefold() == SummarizationMehods(0).name.casefold():
        summary = summary_with_lsa(text , num_sentences)
    elif method.casefold()==SummarizationMehods(1).name.casefold():
        summary = summary_with_text_rank(text , num_sentences )
    elif method.casefold() == SummarizationMehods(2).name.casefold():
        summary = summary_with_text_reduction(text , num_sentences)
        
    elif method.casefold() == SummarizationMehods(3).name.casefold():
        summary = summary_with_tfidf(text , num_sentences)
        
    return summary

demo = gr.Interface(
    fn=summary,
    
    inputs=[gr.TextArea() , gr.Slider(minimum=1 , maximum=10 , step=1) , 
            gr.Dropdown(choices=[SummarizationMehods(0).name ,SummarizationMehods(1).name ,
                                 SummarizationMehods(2).name , SummarizationMehods(3).name])],
    outputs=gr.Text()
)

if __name__ == '__main__':
    
    demo.launch()