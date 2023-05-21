#!/usr/bin/env python3

import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")
model='gpt-3.5-turbo'

def get_completion(prompt, model='gpt-3.5-turbo', temperature=0):
    messages = [{'role': "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model='gpt-3.5-turbo', temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


messages = [
  {'role':'system', 'content':'You are friendly chatbot.'},
  {'role':'user', 'content':'Hi, my name is Isa'},
  {'role':'assistant', 'content':"Hi Isa! It's nice to meet you \
      Is there anything I can help you with today?"},
  {'role':'user', 'content':'Yes, you can remind me, What is my name?'},
]

response = get_completion_from_messages(messages, temperature=1)
print (response)
