# 从函数返回多个值

在 Python 中，当你需要一个函数返回多个值时，有一个便捷的解决方案：返回一个元组（tuple）。元组是 Python 中的一种数据结构，它是一个不可变序列，这意味着一旦创建了元组，就不能更改其元素。元组很有用，因为它们可以在一个地方存储不同类型的多个值。

让我们创建一个函数来解析格式为 `name=value` 的配置行。这个函数的目标是接收这种格式的一行，并将名称和值作为单独的项返回。

1. 首先，你需要创建一个新的 Python 文件。这个文件将包含我们函数的代码和测试代码。在项目目录中，创建一个名为 `return_values.py` 的文件。你可以在终端中使用以下命令来创建这个文件：

```
touch ~/project/return_values.py
```

2. 现在，在你的代码编辑器中打开 `return_values.py` 文件。在这个文件中，我们将编写 `parse_line` 函数。这个函数将一行作为输入，在第一个 '=' 符号处将其分割，并将名称和值作为元组返回。

```python
def parse_line(line):
    """
    Parse a line in the format 'name=value' and return both the name and value.

    Args:
        line (str): Input line to parse in the format 'name=value'

    Returns:
        tuple: A tuple containing (name, value)
    """
    parts = line.split('=', 1)  # Split at the first equals sign
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Return as a tuple
```

在这个函数中，`split` 方法用于在第一个 '=' 符号处将输入行分成两部分。如果该行是正确的 `name=value` 格式，我们将提取名称和值，并将它们作为元组返回。

3. 定义函数后，我们需要添加一些测试代码，以查看函数是否按预期工作。测试代码将使用示例输入调用 `parse_line` 函数并打印结果。

```python
# Test the parse_line function
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # Unpacking the tuple into separate variables
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

在测试代码中，我们首先调用 `parse_line` 函数，并将返回的元组存储在 `result` 变量中。然后我们打印这个元组。接下来，我们使用元组解包（tuple unpacking）将元组的元素直接分配给 `name` 和 `value` 变量，并分别打印它们。

4. 编写完函数和测试代码后，保存 `return_values.py` 文件。然后，打开终端并运行以下命令来执行 Python 脚本：

```
python ~/project/return_values.py
```

你应该会看到类似于以下的输出：

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**解释：**

- `parse_line` 函数使用 `split` 方法在 '=' 字符处分割输入字符串。这个方法根据指定的分隔符将字符串分成多个部分。
- 它使用 `return (name, value)` 语法将两个部分作为元组返回。元组是一种将多个值组合在一起的方式。
- 调用函数时，你有两种选择。你可以将整个元组存储在一个变量中，就像我们对 `result` 变量所做的那样。或者你可以使用 `name, value = parse_line(...)` 语法将元组直接“解包”到单独的变量中。这使得处理单个值更加容易。

这种将多个值作为元组返回的模式在 Python 中非常常见。它使函数更加通用，因为它们可以向调用它们的代码提供多个信息。
