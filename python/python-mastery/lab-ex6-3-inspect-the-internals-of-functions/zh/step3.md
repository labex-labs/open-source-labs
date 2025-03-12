# 在类中应用函数检查

现在，我们将运用所学的函数检查知识来改进类的实现。函数检查能让我们深入了解函数的结构，比如它们所接受的参数。在这个例子中，我们将利用它让类代码更高效且更不易出错。我们会修改 `Structure` 类，使其能自动从 `__init__` 方法的签名中检测字段名。

## 理解 `Structure` 类

`structure.py` 文件中包含一个 `Structure` 类。这个类是一个基类，这意味着其他类可以继承它来创建结构化的数据对象。目前，要定义从继承自 `Structure` 的类创建的对象的属性，我们需要设置一个 `_fields` 类变量。

让我们在编辑器中打开这个文件。我们可以使用以下命令导航到项目目录：

```bash
cd ~/project
```

运行此命令后，你可以在 WebIDE 中的 `structure.py` 文件里找到并查看现有的 `Structure` 类。

## 创建 `Stock` 类

让我们创建一个继承自 `Structure` 类的 `Stock` 类。继承意味着 `Stock` 类将拥有 `Structure` 类的所有特性，并且还能添加自己的特性。我们将以下代码添加到 `structure.py` 文件的末尾：

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

然而，这种方法存在一个问题。我们必须同时定义 `_fields` 元组和 `__init__` 方法，且参数名要相同。这是多余的，因为我们本质上是在重复编写相同的信息。如果在修改其中一个时忘记更新另一个，就可能会导致错误。

## 添加 `set_fields` 类方法

为了解决这个问题，我们将在 `Structure` 类中添加一个 `set_fields` 类方法。这个方法将自动从 `__init__` 方法的签名中检测字段名。以下是需要添加到 `Structure` 类中的代码：

```python
@classmethod
def set_fields(cls):
    # Get the signature of the __init__ method
    import inspect
    sig = inspect.signature(cls.__init__)

    # Get parameter names, skipping 'self'
    params = list(sig.parameters.keys())[1:]

    # Set _fields attribute on the class
    cls._fields = tuple(params)
```

这个方法使用了 `inspect` 模块，它是 Python 中用于获取函数和类等对象信息的强大工具。首先，它获取 `__init__` 方法的签名。然后，它提取参数名，但跳过 `self` 参数，因为 `self` 是 Python 类中引用实例本身的特殊参数。最后，它用这些参数名设置 `_fields` 类变量。

## 修改 `Stock` 类

现在我们有了 `set_fields` 方法，就可以简化 `Stock` 类了。用以下代码替换之前的 `Stock` 类代码：

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

这样，我们就不必手动定义 `_fields` 元组了。`set_fields` 方法会为我们处理这个问题。

## 测试修改后的类

为了确保修改后的类能正常工作，我们将创建一个简单的测试脚本。创建一个名为 `test_structure.py` 的新文件，并添加以下代码：

```python
from structure import Stock

def test_stock():
    # Create a Stock object
    s = Stock(name='GOOG', shares=100, price=490.1)

    # Test string representation
    print(f"Stock representation: {s}")

    # Test attribute access
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")

    # Test attribute modification
    s.shares = 50
    print(f"Updated shares: {s.shares}")

    # Test attribute error
    try:
        s.share = 50  # Misspelled attribute
        print("Error: Did not raise AttributeError")
    except AttributeError as e:
        print(f"Correctly raised: {e}")

if __name__ == "__main__":
    test_stock()
```

这个测试脚本创建了一个 `Stock` 对象，测试了它的字符串表示形式，访问了它的属性，修改了一个属性，并尝试访问一个拼写错误的属性，以检查是否会引发正确的错误。

要运行测试脚本，请使用以下命令：

```bash
python3 test_structure.py
```

你应该会看到类似以下的输出：

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## 工作原理

1. `set_fields` 方法使用 `inspect.signature()` 从 `__init__` 方法中获取参数名。这个函数为我们提供了 `__init__` 方法参数的详细信息。
2. 然后，它根据这些参数名自动设置 `_fields` 类变量。这样，我们就不必在两个不同的地方编写相同的参数名了。
3. 这消除了手动定义 `_fields` 和 `__init__` 并使参数名匹配的需求。它让我们的代码更易于维护，因为如果我们修改了 `__init__` 方法中的参数，`_fields` 会自动更新。

这种方法利用函数检查让我们的代码更易于维护且更不易出错。这是 Python 自省能力的一个实际应用，它允许我们在运行时检查和修改对象。
