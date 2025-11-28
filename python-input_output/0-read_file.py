#!/usr/bin/python3
def read_file(text):
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
