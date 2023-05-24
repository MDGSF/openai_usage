#!/usr/bin/env python3

import openai
import os
import argparse
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

parser = argparse.ArgumentParser(description='OpenAI ChatGPT')
parser.add_argument('-m', '--prompt', help='prompt message send to ChatGPT')
parser.add_argument('-f', '--prompt_file', help='prompt file content will be send to ChatGPT')
args = parser.parse_args()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = {
  "http": "http://192.168.60.1:1080",
  "https": "http://192.168.60.1:1080"
}

def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role': "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

if args.prompt and len(args.prompt) > 0:
    prompt = args.prompt
    response = get_completion(prompt)
    print (response)
elif args.prompt_file and len(args.prompt_file) > 0:
    prompt_file = open(args.prompt_file, 'r')
    prompt_file_content = prompt_file.read()
    prompt_file.close()
    prompt = prompt_file_content
    response = get_completion(prompt)
    print (response)
else:
  print (f'Nothing happen! ./gpt.py -h will show you some help message!')
  pass

