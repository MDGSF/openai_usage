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

### Tactic 2: Ask for structured output

HTML, JSON

### Tactic 3: Check whether conditions are satisfied

Check assumptions required to do the task.

### Tactic 4: Few-shot prompting

Give successful examples of completing tasks.
Then ask model to perform the task.

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

- `summarize_01.py`
- `summarize_02.py`
- `summarize_03.py`
- `extract_01.py`

## Inferring




