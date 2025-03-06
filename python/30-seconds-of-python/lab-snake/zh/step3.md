# 处理更复杂的模式

我们当前的函数可以处理驼峰命名法（camelCase），但还需要对其进行增强，以处理其他模式，例如：

1. 帕斯卡命名法（PascalCase）（例如，`HelloWorld`）
2. 带有连字符的字符串（例如，`hello-world`）
3. 已经包含下划线的字符串（例如，`hello_world`）

让我们更新函数以处理这些情况：

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern (sequences of uppercase letters)
    s = re.sub('([A-Z]+)', r' \1', s)

    # Handle camelCase pattern (lowercase followed by uppercase)
    s = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Split by spaces, join with underscores, and convert to lowercase
    return '_'.join(s.split()).lower()

# Test with multiple examples
if __name__ == "__main__":
    test_strings = [
        "helloWorld",
        "HelloWorld",
        "hello-world",
        "hello_world",
        "some text"
    ]

    for test in test_strings:
        result = snake(test)
        print(f"Original: {test}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

我们所做的改进如下：

1. 首先，将所有连字符替换为空格。
2. 新的正则表达式 `re.sub('([A-Z]+)', r' \1', s)` 在任何连续的大写字母序列前添加一个空格，这有助于处理帕斯卡命名法。
3. 保留处理驼峰命名法的正则表达式。
4. 最后，按空格分割字符串，用下划线连接，并转换为小写，这样可以处理剩余的空格并确保输出格式一致。

运行脚本，用各种输入格式进行测试：

```bash
python3 ~/project/snake_case.py
```

你应该会看到如下输出：

```
Original: helloWorld
Snake case: hello_world
--------------------
Original: HelloWorld
Snake case: hello_world
--------------------
Original: hello-world
Snake case: hello_world
--------------------
Original: hello_world
Snake case: hello_world
--------------------
Original: some text
Snake case: some_text
--------------------
```

我们的函数现在更加健壮，可以处理各种输入格式。下一步，我们将进行最后的优化，并使用完整的测试套件进行测试。
