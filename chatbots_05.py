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

def collect_messages(_):
  prompt = inp.value_input
  inp.value = ''
  context.append({'role':'user', 'content':f"{prompt}"})
  response = get_completion_from_messages(context)
  context.append({'role':'assistant', 'content':f"{response}"})
  panels.append(pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
  panels.append(pn.Row('Assistant:', pn.pane.Markdown(response, width=600)))
  return pn.Column(*panels)


response = get_completion_from_messages(messages, temperature=1)
print (response)
