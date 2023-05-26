#!/usr/bin/env python3

'''
使用说明：
1. 需要配置环境变量 OPENAI_API_KEY="xxx"，这个 key 需要从 openai 的后台自己拿，
  所以你需要一个 openai 的账号才行。
2. 需要修改下面的代理，修改为你自己本地的代理地址。
  openai.proxy = {
    "http": "http://127.0.0.1:1080",
    "https": "http://127.0.0.1:1080"
  }

使用方法：
1. 需要安装 python3
2. 需要安装如下两个依赖
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple openai
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-dotenv
3. 把该文件放到 PATH 路径下面，并添加可执行权限 chmod a+x gpt.py
4. 使用方法一：直接在命令行写 prompt
  gpt.py -m "hello world"
4. 使用方法二：把 prompt 写到文件中
  gpt.py -f prompt.txt
'''

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

