# 使用继承构建验证系统

在这一步中，我们将使用继承构建一个实用的验证系统。继承是编程中一个强大的概念，它允许你基于现有的类创建新的类。通过这种方式，你可以复用代码，创建更有条理和模块化的程序。通过构建这个验证系统，你将了解如何使用继承来创建可复用的代码组件，并以不同的方式组合它们。

## 创建基础验证器类

首先，我们需要为验证器创建一个基类。为此，我们将在 WebIDE 中创建一个新文件。你可以这样操作：点击“File” > “New File”，或者使用键盘快捷键。新文件打开后，将其命名为 `validate.py`。

现在，让我们在这个文件中添加一些代码，以创建一个基础的 `Validator` 类。这个类将作为我们所有其他验证器的基础。

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

在这段代码中，我们定义了一个 `Validator` 类，其中包含一个 `check` 方法。`check` 方法接受一个值作为参数，并直接返回该值，不做任何修改。`@classmethod` 装饰器用于将这个方法定义为类方法。这意味着我们可以直接在类上调用这个方法，而无需创建类的实例。

## 添加类型验证器

接下来，我们将添加一些用于检查值类型的验证器。这些验证器将继承自我们刚刚创建的 `Validator` 类。回到 `validate.py` 文件，添加以下代码：

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

`Typed` 类是 `Validator` 类的子类。它有一个 `expected_type` 属性，初始值设置为 `object`。`Typed` 类中的 `check` 方法会检查给定的值是否为预期的类型。如果不是，它会抛出一个 `TypeError` 异常。如果类型正确，它会使用 `super().check(value)` 调用父类的 `check` 方法。

`Integer`、`Float` 和 `String` 类继承自 `Typed` 类，并指定了它们要检查的确切类型。例如，`Integer` 类会检查一个值是否为整数。

## 测试类型验证器

现在我们已经创建了类型验证器，让我们来测试它们。打开一个新的终端，运行以下命令启动 Python 解释器：

```bash
python3
```

Python 解释器启动后，我们可以导入并测试我们的验证器。以下是一些用于测试的代码：

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

运行这段代码时，你应该会看到类似以下的输出：

```
10
Error: Expected <class 'int'>
'10'
```

我们还可以在函数中使用这些验证器。让我们试试看：

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

运行这段代码时，你应该会看到：

```
4
Error: Expected <class 'int'>
```

## 添加值验证器

到目前为止，我们已经创建了用于检查值类型的验证器。现在，让我们添加一些用于检查值本身而不是类型的验证器。回到 `validate.py` 文件，添加以下代码：

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

`Positive` 验证器用于检查一个值是否为非负数。如果值小于 0，它会抛出一个 `ValueError` 异常。`NonEmpty` 验证器用于检查一个值的长度是否不为 0。如果长度为 0，它会抛出一个 `ValueError` 异常。

## 使用多继承组合验证器

现在，我们将使用多继承来组合我们的验证器。多继承允许一个类从多个父类继承。回到 `validate.py` 文件，添加以下代码：

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

这些新类将类型检查和值检查组合在一起。例如，`PositiveInteger` 类会检查一个值是否既是整数又是非负数。这里继承的顺序很重要。验证器将按照类定义中指定的顺序进行检查。

## 测试组合验证器

让我们测试我们的组合验证器。在 Python 解释器中，运行以下代码：

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

运行这段代码时，你应该会看到：

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

这展示了我们如何组合验证器来创建更复杂的验证规则。

测试完成后，你可以运行以下命令退出 Python 解释器：

```python
exit()
```
