# 添加数学运算

目前，我们的 `MutInt` 类不支持加法等数学运算。在 Python 中，要为自定义类启用此类运算，我们需要实现特殊方法。这些特殊方法也被称为 “魔术方法” 或 “双下划线方法”，因为它们被双下划线包围。让我们通过实现算术运算的相关特殊方法来添加加法功能。

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
        # For commutative operations like +, we can reuse __add__
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in-place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

我们为 `MutInt` 类添加了三个新方法：

- `__add__()`：当 `+` 运算符用于 `MutInt` 对象在左侧时，会调用此方法。在该方法内部，我们首先检查 `other` 操作数是 `MutInt` 实例还是 `int` 类型。如果是，则执行加法并返回一个包含结果的新 `MutInt` 对象。如果 `other` 操作数是其他类型，我们返回 `NotImplemented`。这会告诉 Python 尝试其他方法或抛出 `TypeError`。
- `__radd__()`：当 `+` 运算符用于 `MutInt` 对象在右侧时，会调用此方法。由于加法是可交换运算（即 `a + b` 与 `b + a` 相同），我们可以直接复用 `__add__` 方法。
- `__iadd__()`：当 `+=` 运算符用于 `MutInt` 对象时，会调用此方法。它不会创建新对象，而是修改现有的 `MutInt` 对象并返回它。

2. 创建一个名为 `test_math_ops.py` 的新测试文件，来测试这些新方法：

```python
# test_math_ops.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(5)

# Test regular addition
c = a + b
print(f"a + b = {c}")

# Test addition with int
d = a + 10
print(f"a + 10 = {d}")

# Test reversed addition
e = 7 + a
print(f"7 + a = {e}")

# Test in-place addition
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# Test in-place addition with reference sharing
f = a  # f and a point to the same object
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# Test unsupported operation
try:
    result = a + 3.5  # Adding a float is not supported
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

在这个测试文件中，我们首先导入 `MutInt` 类。然后创建一些 `MutInt` 对象并执行不同类型的加法运算。我们还测试了原地加法以及尝试不支持的运算（添加浮点数）的情况。

3. 运行测试脚本：

```bash
python3 /home/labex/project/test_math_ops.py
```

你应该会看到类似以下的输出：

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

现在我们的 `MutInt` 类支持基本的加法运算。注意，当我们使用 `+=` 时，`a` 和 `f` 都被更新了。这表明 `a += 10` 修改了现有对象，而不是创建了一个新对象。

这种可变对象的行为类似于 Python 的内置可变类型，如列表。例如：

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # Both a and b are updated
```

相比之下，对于元组等不可变类型，`+=` 会创建一个新对象：

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c is a new object, d still points to the old one
```
