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


user_messages = [
  "My screen is flickering.",
  "Mi pantalla está parpadeando.",
  "Mon écran clignote.",
  "我的屏幕在闪烁"
]

for issue in user_messages:
  prompt = f"Tell me what language this is: ```{issue}```"
  lang = get_completion(prompt)
  print(f"Original message ({lang}): {issue}")

  prompt = f"""
  Translate the following text to English \
  and Korean: ```{issue}```
  """
  response = get_completion(prompt)
  print (response)
