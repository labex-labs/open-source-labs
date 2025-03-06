# 使用正则表达式进行模式匹配

为了将字符串转换为蛇形命名法（snake case），我们将使用正则表达式（regex）来识别单词边界。Python 中的 `re` 模块提供了强大的模式匹配功能，可用于此任务。

让我们更新函数以处理驼峰命名法（camelCase）的字符串：

1. 首先，你需要识别小写字母后面跟着大写字母的模式（例如 “camelCase”）。
2. 然后，在它们之间插入一个空格。
3. 最后，将所有内容转换为小写，并将空格替换为下划线。

使用以下改进后的函数更新你的 `snake_case.py` 文件：

```python
import re

def snake(s):
    # Replace pattern of a lowercase letter followed by uppercase with lowercase, space, uppercase
    s1 = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Replace spaces with underscores and convert to lowercase
    return s1.lower().replace(' ', '_')

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

让我们详细分析这个函数的工作原理：

- `re.sub('([a-z])([A-Z])', r'\1 \2', s)` 查找小写字母 `([a-z])` 后面跟着大写字母 `([A-Z])` 的模式。然后，它将此模式替换为相同的字母，但使用 `\1` 和 `\2` 在它们之间添加一个空格，`\1` 和 `\2` 分别引用捕获的组。
- 然后，我们使用 `lower()` 将所有内容转换为小写，并将空格替换为下划线。

再次运行脚本，看看它是否能处理驼峰命名法的字符串：

```bash
python3 ~/project/snake_case.py
```

现在的输出应该是：

```
Original: helloWorld
Snake case: hello_world
```

很棒！我们的函数现在可以处理驼峰命名法的字符串了。下一步，我们将对其进行增强，以处理更复杂的情况。
