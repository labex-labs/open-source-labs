# 改进对象表示

我们的 `Structure` 类对于创建和访问对象很有用。然而，目前它没有一种很好的方式将自身表示为字符串。当你打印一个对象或在 Python 解释器中查看它时，你希望看到一个清晰且信息丰富的显示。这有助于你理解对象是什么以及它的值是什么。

## 理解 Python 的对象表示

在 Python 中，有两个特殊方法用于以不同方式表示对象。这些方法很重要，因为它们允许你控制对象的显示方式。

- `__str__`：此方法由 `str()` 函数和 `print()` 函数使用。它提供对象的人类可读表示。例如，如果你有一个 `Stock` 对象，`__str__` 方法可能返回类似 "Stock: GOOG, 100 shares at $490.1" 的内容。
- `__repr__`：此方法由 Python 解释器和 `repr()` 函数使用。它提供对象更具技术性且明确的表示。`__repr__` 的目标是提供一个可用于重新创建对象的字符串。例如，对于一个 `Stock` 对象，它可能返回 "Stock('GOOG', 100, 490.1)"。

让我们为我们的 `Structure` 类添加一个 `__repr__` 方法。这将使调试代码变得更容易，因为我们可以清楚地看到对象的状态。

## 实现良好的表示

现在，你需要更新你的 `structure.py` 文件。你将为 `Structure` 类添加 `__repr__` 方法。此方法将创建一个字符串，以可用于重新创建对象的方式表示该对象。

```python
def __repr__(self):
    """
    Return a representation of the object that can be used to recreate it.
    Example: Stock('GOOG', 100, 490.1)
    """
    # Get the class name
    cls_name = type(self).__name__

    # Get all the field values
    values = [getattr(self, name) for name in self._fields]

    # Format the fields and values
    args_str = ', '.join(repr(value) for value in values)

    # Return the formatted string
    return f"{cls_name}({args_str})"
```

此方法的具体步骤如下：

1. 它使用 `type(self).__name__` 获取类名。这很重要，因为它能告诉你正在处理的是哪种对象。
2. 它从实例中检索所有字段的值。这能让你获取对象所持有的数据。
3. 它创建一个包含类名和值的字符串表示。这个字符串可用于重新创建对象。

## 测试改进后的表示

让我们测试我们改进后的实现。创建一个名为 `test_repr.py` 的新文件。这个文件将创建我们类的一些实例并打印它们的表示。

```python
# test_repr.py
from structure import Stock, Point, Date

# Create instances
s = Stock('GOOG', 100, 490.1)
p = Point(3, 4)
d = Date(2023, 11, 9)

# Print the representations
print(repr(s))
print(repr(p))
print(repr(d))

# Direct printing also uses __repr__ in the interpreter
print(s)
print(p)
print(d)
```

要运行测试，请打开终端并输入以下命令：

```bash
python3 test_repr.py
```

你应该会看到以下输出：

```
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
```

这个输出比以前更具信息性。当你看到 `Stock('GOOG', 100, 490.1)` 时，你立即知道该对象代表什么。你甚至可以复制这个字符串并在代码中使用它来重新创建对象。

## 良好表示的好处

一个良好的 `__repr__` 实现对于调试非常有帮助。当你在解释器中查看对象或在程序执行期间记录它们时，清晰的表示能让你更快地识别问题。你可以看到对象的确切状态并理解可能出现的问题。
