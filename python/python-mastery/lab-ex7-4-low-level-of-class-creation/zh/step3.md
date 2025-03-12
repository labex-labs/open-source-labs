# 高效的类生成

既然你已经了解了如何使用 `type()` 函数创建类，我们将探索一种更高效的方法来生成多个相似的类。这种方法可以节省你的时间并减少代码重复，让你的编程过程更加顺畅。

## 理解现有的验证器类

首先，你需要在 WebIDE 中打开 `validate.py` 文件。该文件已经包含了几个验证器类，用于检查值是否满足特定条件。这些类包括 `Validator`、`Positive`、`PositiveInteger` 和 `PositiveFloat`。我们将在这个文件中添加一个 `Typed` 基类和几个特定类型的验证器。

要打开文件，请在终端中运行以下命令：

```bash
cd ~/project
```

## 添加 `Typed` 验证器类

让我们从添加 `Typed` 验证器类开始。这个类将用于检查一个值是否为预期的类型。

```python
class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)
```

在这段代码中，`expected_type` 默认设置为 `object`。子类将用它们要检查的特定类型覆盖这个值。`check` 方法使用 `isinstance` 函数来检查值是否为预期的类型。如果不是，则会引发一个 `TypeError`。

传统上，我们会像这样创建特定类型的验证器：

```python
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

然而，这种方法存在重复。我们可以使用 `type()` 构造函数动态生成这些类，从而做得更好。

## 动态生成类型验证器

我们将用一种更高效的方法替换单个类的定义。

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

这段代码的作用如下：

1. 定义一个元组列表。每个元组包含一个类名和对应的 Python 类型。
2. 使用带有 `type()` 函数的生成器表达式来创建每个类。`type()` 函数接受三个参数：类名、基类元组和类属性字典。
3. 使用 `globals().update()` 将新创建的类添加到全局命名空间中。这使得这些类在整个模块中都可以访问。

你完成后的 `validate.py` 文件应该类似于以下内容：

```python
# Basic validator classes

class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check(cls, value):
        pass

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value <= 0:
            raise ValueError('Expected a positive value')
        super().check(value)

class PositiveInteger(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        super().check(value)

class PositiveFloat(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, float):
            raise TypeError('Expected a float')
        super().check(value)

class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)

# Generate type validators dynamically
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

## 测试动态生成的类

现在，让我们测试我们动态生成的验证器类。首先，打开一个 Python 交互式 shell。

```bash
cd ~/project
python3
```

进入 Python shell 后，导入并测试我们的验证器。

```python
from validate import Integer, Float, String

# Test the Integer validator
i = Integer()
i.__set_name__(None, 'test_int')
try:
    i.check("not an integer")
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"Integer validation: {e}")

# Test the String validator
s = String()
s.__set_name__(None, 'test_str')
try:
    s.check(123)
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"String validation: {e}")

# Add a new validator class to the list
import sys
print("Current validator classes:", [cls for cls in dir() if cls in ['Integer', 'Float', 'String']])
```

你应该会看到显示类型验证错误的输出。这表明我们动态生成的类正在正确工作。

测试完成后，退出 Python shell：

```python
exit()
```

## 扩展动态类生成

如果你想添加更多的类型验证器，只需更新 `validate.py` 中的 `_typed_classes` 列表。

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str),
    ('List', list),
    ('Dict', dict),
    ('Bool', bool)
]
```

这种方法提供了一种强大而高效的方式来生成多个相似的类，而无需编写重复的代码。它允许你在需求增长时轻松扩展你的应用程序。
