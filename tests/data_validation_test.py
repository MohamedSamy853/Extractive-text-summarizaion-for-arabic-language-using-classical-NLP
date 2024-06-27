import pytest 
from datasets import load_from_disk

import re  , string
from textacy.preprocessing.resources import (RE_EMAIL , RE_URL , RE_NUMBER ,
                                              RE_NUMBER , RE_EMOJI , RE_SHORT_URL , RE_PHONE_NUMBER
                                            )


cleaned_dataset = load_from_disk("./datasets/cleaned_xlsum_arabic")

RE_NON_ARABIC = re.compile(r"[%s]"%string.ascii_letters)

def check_regex(regex , name):
    for split in ['train' , 'validation' , 'test']:
        for col in ['text', 'summary']:
            assert any([bool(re.findall(regex , text)) for text in cleaned_dataset[split][col]])  == False \
                , f"there are {name} in {split} in {col} column"
    

def test_email():
    
    check_regex(RE_EMAIL , "emails")
   
def test_url():
    
    check_regex(RE_URL , "urls")

def test_short_url():
  
    check_regex(RE_SHORT_URL , "short urls")

def test_emoji():
    
    check_regex(RE_EMOJI , "emoji")
    
def test_number():
    
    check_regex(RE_NUMBER , "numbers")

def test_phone_number():
    
    check_regex(RE_PHONE_NUMBER , 'phone numbers')

def test_english_letters():
   
   check_regex(RE_NON_ARABIC , 'english words')


