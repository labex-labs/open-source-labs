# 添加类型转换

我们的 `MutInt` 类目前支持加法和比较运算。但是，它不能与 Python 的内置转换函数（例如 `int()` 和 `float()`）一起使用。这些转换函数在 Python 中非常有用。例如，当你想要将一个值转换为整数或浮点数以进行不同的计算或操作时，你需要依赖这些函数。因此，让我们为 `MutInt` 类添加与它们一起使用的功能。

1.  在 WebIDE 中打开 `mutint.py`，并使用以下代码更新它：

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index

    def __lshift__(self, other):
        """Handle left shift: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Handle reversed left shift: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

我们向 `MutInt` 类添加了三个新方法：

1.  `__int__()`: 当你在我们的 `MutInt` 类的对象上使用 `int()` 函数时，会调用此方法。例如，如果你有一个 `MutInt` 对象 `a`，并且你编写了 `int(a)`，Python 将调用 `a` 对象的 `__int__()` 方法。
2.  `__float__()`: 类似地，当你在我们的 `MutInt` 对象上使用 `float()` 函数时，会调用此方法。
3.  `__index__()`: 此方法用于专门需要整数索引的操作。例如，当你想要使用索引访问列表中的元素，或执行位长度操作时，Python 需要一个整数索引。
4.  `__lshift__()`: 当 `MutInt` 对象位于 `<<` 运算符的左侧时，此方法处理左移操作。
5.  `__rlshift__()`: 当 `MutInt` 对象位于 `<<` 运算符的右侧时，此方法处理左移操作。

`__index__` 方法对于需要整数索引的操作至关重要，例如列表索引、切片和位长度操作。在我们的简单实现中，我们将其设置为与 `__int__` 相同，因为我们的 `MutInt` 对象的值可以直接用作整数索引。

`__lshift__` 和 `__rlshift__` 方法对于支持按位左移操作至关重要。它们允许我们的 `MutInt` 对象参与按位运算，这是类整数类型（integer-like types）的常见要求。

2.  创建一个名为 `test_conversions.py` 的新测试文件来测试这些新方法：

```python
# test_conversions.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test conversions
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Test using as an index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Test using in bit operations (requires __index__)
print(f"1 << a: {1 << a}")  # Shift left by 3

# Test hex/oct/bin functions (requires __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modify and test again
a.value = 4
print(f"\nAfter changing value to 4:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3.  运行测试脚本：

```bash
python3 /home/labex/project/test_conversions.py
```

你应该看到类似于这样的输出：

```
int(a): 3
float(a): 3.0
names[a]: Thomas
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 4:
int(a): 4
names[a]: Lewis
```

现在，我们的 `MutInt` 类可以转换为标准 Python 类型，并用于需要整数索引的操作。

`__index__` 方法尤为重要。它是在 Python 中引入的，允许对象在需要整数索引的情况下使用，例如列表索引、按位运算和各种函数（如 `hex()`、`oct()` 和 `bin()`）。

通过这些添加，我们的 `MutInt` 类现在是一个相当完整的原始类型（primitive type）。它可以在大多数可以使用常规整数的上下文中使用，并且具有可变的额外好处。

## 完整的 MutInt 实现

这是我们完整的 `MutInt` 实现，包含我们添加的所有功能：

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index

    def __lshift__(self, other):
        """Handle left shift: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Handle reversed left shift: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

此实现涵盖了在 Python 中创建新原始类型（primitive type）的关键方面。为了使其更加完整，你可以为其他操作（如减法、乘法、除法等）实现其他方法。
