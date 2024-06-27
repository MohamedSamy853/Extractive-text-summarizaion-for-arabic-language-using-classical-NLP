import re  , string
from textacy.preprocessing.resources import (RE_EMAIL , RE_URL , RE_NUMBER ,
                                              RE_NUMBER , RE_EMOJI , RE_SHORT_URL , RE_PHONE_NUMBER
                                            )

NON_ARABIC_RE = re.compile(r"[%s]"%string.ascii_letters)

def clean_text(text:str)->str:
    '''remove unwanted data'''
    patterns = [RE_EMAIL , RE_EMOJI , RE_NUMBER , RE_PHONE_NUMBER , RE_SHORT_URL , RE_URL , NON_ARABIC_RE]
    
    for pattern in patterns:
        
        text = pattern.sub("" , text)
        
    return text

    