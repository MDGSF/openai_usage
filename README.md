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

