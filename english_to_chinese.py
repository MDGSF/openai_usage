#!/usr/bin/env python3

import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")
model='gpt-3.5-turbo'

def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role': "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

text = f"""
<grandparent>: The river that carves the deepest \
valley flows from a modest spring: the \
grandest symphony originates from a single note; \
the nost intricate tapestry begins with a solitary thread.
"""
prompt = f"""
Translate the text delimited by triple backticks \
into Chinese.
```{text}```
"""
response = get_completion(prompt)
print (response)
