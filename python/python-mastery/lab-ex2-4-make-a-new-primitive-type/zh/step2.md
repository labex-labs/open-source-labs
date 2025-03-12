# 改进字符串表示形式

当你在 Python 中打印一个 `MutInt` 对象时，你会看到类似 `<__main__.MutInt object at 0x...>` 这样的输出。这个输出没什么用，因为它没有告诉你 `MutInt` 对象的实际值。为了让你更容易理解这个对象代表什么，我们将为字符串表示形式实现特殊方法。

1. 在 WebIDE 中打开 `mutint.py` 文件，并使用以下代码更新它：

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value

    def __str__(self):
        """Return a string representation for printing."""
        return str(self.value)

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)
```

我们为 `MutInt` 类添加了三个重要的方法：

- `__str__()`：当你对对象使用 `str()` 函数或直接打印对象时，会调用这个方法。它应该返回一个人类可读的字符串。
- `__repr__()`：这个方法提供对象的 “官方” 字符串表示形式。它主要用于调试，理想情况下应该返回一个字符串，如果将这个字符串传递给 `eval()` 函数，应该能重新创建该对象。
- `__format__()`：这个方法允许你对 `MutInt` 对象使用 Python 的字符串格式化系统。你可以使用诸如填充和数字格式化之类的格式说明符。

2. 创建一个名为 `test_string_repr.py` 的新测试文件，来测试这些新方法：

```python
# test_string_repr.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test string representation
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# Test direct printing
print(f"Print a: {a}")

# Test string formatting
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# Test mutability
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

在这个测试文件中，我们首先导入 `MutInt` 类。然后创建一个值为 `3` 的 `MutInt` 对象。我们通过使用 `str()` 和 `repr()` 函数来测试 `__str__()` 和 `__repr__()` 方法。我们还测试了直接打印、字符串格式化以及 `MutInt` 对象的可变性。

3. 运行测试脚本：

```bash
python3 /home/labex/project/test_string_repr.py
```

当你运行这个命令时，Python 将执行 `test_string_repr.py` 脚本。你应该会看到类似以下的输出：

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

现在我们的 `MutInt` 对象显示效果很好。字符串表示形式展示了其底层的值，并且我们可以像处理普通整数一样使用字符串格式化。

`__str__()` 和 `__repr__()` 的区别在于，`__str__()` 旨在产生一个对人类友好的输出，而 `__repr__()` 理想情况下应该产生一个字符串，当将其传递给 `eval()` 函数时，能够重新创建该对象。这就是为什么我们在 `__repr__()` 方法中包含了类名。

`__format__()` 方法使我们的对象能够与 Python 的格式化系统配合使用，因此我们可以使用诸如填充和数字格式化之类的格式说明符。
