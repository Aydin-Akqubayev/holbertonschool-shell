#!/usr/bin/python3
def multiple_returns(text):
    length_text = len(text)
    if length_text == 0:
        first_text = None
    else:
        first_text = text[0]
    return length_text, first_text
