# openai_usage

```sh
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple openai
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-dotenv
```

## Principle 1

Write clear and specific instructions

### Tactic 1: Use delimiters

- Triple quotes: """
- Triple backticks: ```
- Triple dashes: ---
- Angle brackets: < >
- XML tags: `<tag> </tag>`

- `demo01.py`

### Tactic 2: Ask for structured output

HTML, JSON

- `demo02.py`

### Tactic 3: Check whether conditions are satisfied

Check assumptions required to do the task.

- `demo03.py`

### Tactic 4: Few-shot prompting

Give successful examples of completing tasks.
Then ask model to perform the task.

- `demo04.py`

## Principle 2

Give the model time to think

### Tactic 1: Specify the steps to complete a task

```text
Step 1: ...
Step 2: ...
...
Step N: ...
```

- `demo05.py`
- `demo06.py`

### Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion

- `demo07.py`
- `demo08.py`

## Model Limitations

- Hallucination
- Makes statements that sound plausible but are not true
- Reducing hallucinations:
- First find relevant information,
- then answer the question
- based on the relevant information.

- `demo09.py`

## Iterative Prompt Development

Prompt guidelines:

- Be clear and specific
- Analyze why result does not give desired output.
- Refine the idea and the prompt
- Repeat

Iterative Process:

- Try something
- Analyze where the result does not give what your want
- Clarify instructions, give more time to think
- Refine prompts with a batch of examples

## Summarize

总结文本

- `summarize_01.py`
- `summarize_02.py`
- `summarize_03.py`
- `extract_01.py`: 提取文本信息

## Inferring

推理

- `inferring_01.py`: 积极还是消极
- `inferring_02.py`: 提取情绪
- `inferring_03.py`: 判断是否生气
- `inferring_04.py`: 提取商品和品牌
- `inferring_05.py`: 同时提取多个信息
- `inferring_06.py`: 提取主题词语
- `inferring_06.py`: 判断文章和给定主题是否相关

## Transforming

Translating to a different language, and more!

- `transforming_01.py`: 一种语言翻译为另一种语言
- `transforming_02.py`: 判断给定文本是什么语言
- `transforming_03.py`: 一种语言翻译为其它多种语言
- `transforming_04.py`: 翻译为正式和非正式
- `transforming_05.py`: 翻译
- `transforming_06.py`: 把口语转换为正式表达
- `transforming_07.py`: 把JSON转换为HTML
- `transforming_08.py`: 检查语法错误，并修改为正确的
- `transforming_09.py`: 检查语法错误，并修改为正确的
- `transforming_10.py`: 检查语法错误，并修改为正确的
- `transforming_11.py`: 检查语法错误，并修改为正确的

## Expanding

Expand a shorter text to a longer text (email, essay)

- `expanding_email.py`: 回复客户邮件

### Temperature

temperature 是一个随机数，
数字越小，表示结果越确定
数字越大，表示结果越随机

#### example

my favorite food is xxx.

- pizza: 53%
- sushi: 30%
- tacos: 5%

temperature = 0 时，输出可能是：

- my favorite food is pizza
- my favorite food is pizza
- my favorite food is pizza

temperature = 0.3 时，输出可能是：

- my favorite food is pizza
- my favorite food is sushi
- my favorite food is pizza

temperature = 0.7 时，输出可能是：

- my favorite food is tacos
- my favorite food is sushi
- my favorite food is pizza

**Note:**

- for tasks that require reliability, predictability，set temperature = 0
- for tasks that require variety, use temperature higher
- 当 temperature = 0 时，每次都是相同的输出。
- 当 temperature = 0.7 时，每次都会得到不同的输出。

## Chatbots

- `chatbots_01.py`
- `chatbots_02.py`
- `chatbots_03.py`
- `chatbots_04.py`
- `chatbots_05.py`
