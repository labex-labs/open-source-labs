# 理解问题

在编写蛇形命名法（snake case）转换函数之前，让我们先明确需要完成的任务：

1. 你需要将任何格式的字符串转换为蛇形命名法。
2. 蛇形命名法指的是所有字母为小写，单词之间用下划线分隔。
3. 你需要处理不同的输入格式：
   - 驼峰命名法（camelCase）（例如，`camelCase` → `camel_case`）
   - 带有空格的字符串（例如，`some text` → `some_text`）
   - 混合格式的字符串（例如，包含连字符、下划线和大小写混合的情况）

让我们先为蛇形命名法函数创建一个新的 Python 文件。在 WebIDE 中，导航到项目目录并创建一个名为 `snake_case.py` 的新文件：

```python
# This function will convert a string to snake case
def snake(s):
    # We'll implement this function step by step
    pass  # Placeholder for now

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

保存此文件。下一步，我们将开始实现该函数。

现在，让我们运行这个占位函数，确保文件设置正确。打开终端并运行：

```bash
python3 ~/project/snake_case.py
```

![python-prompt](../assets/screenshot-20250306-B5lI9tyo@2x.png)

你应该会看到如下输出：

```
Original: helloWorld
Snake case: None
```

结果为 `None` 是因为当前函数只是返回 Python 的默认 `None` 值。下一步，我们将添加实际的转换逻辑。
