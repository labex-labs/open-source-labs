# 实现抽象基类

在这一步中，我们将使用 Python 的 `abc` 模块把 `TableFormatter` 类转换为一个合适的抽象基类（Abstract Base Class，ABC）。不过，首先让我们了解一下什么是抽象基类以及为什么需要它。

## 理解抽象基类

抽象基类是 Python 中的一种特殊类。它是一种不能直接创建对象的类，也就是说你不能对其进行实例化。抽象基类的主要目的是为其子类定义一个通用接口。它设定了一组所有子类都必须遵循的规则，具体来说，它要求子类实现某些特定的方法。

以下是关于抽象基类的一些关键概念：

- 我们使用 Python 中的 `abc` 模块来创建抽象基类。
- 用 `@abstractmethod` 装饰器标记的方法就像是规则。任何继承自抽象基类的子类都必须实现这些方法。
- 如果你尝试创建一个继承自抽象基类但没有实现所有必需方法的类的对象，Python 将会抛出一个错误。

现在你已经了解了抽象基类的基础知识，让我们看看如何修改 `TableFormatter` 类使其成为一个抽象基类。

## 修改 `TableFormatter` 类

打开 `tableformat.py` 文件。我们将对 `TableFormatter` 类进行一些修改，使其使用 `abc` 模块并成为一个抽象基类。

1. 首先，我们需要从 `abc` 模块导入必要的内容。在文件顶部添加以下导入语句：

```python
# tableformat.py
from abc import ABC, abstractmethod
```

这个导入语句引入了两个重要的内容：`ABC`，它是 Python 中所有抽象基类的基类；以及 `abstractmethod`，这是一个装饰器，我们将用它来标记抽象方法。

2. 接下来，我们将修改 `TableFormatter` 类。它应该继承自 `ABC` 以成为一个抽象基类，并且我们将使用 `@abstractmethod` 装饰器将其方法标记为抽象方法。修改后的类应该如下所示：

```python
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        pass
```

注意这个修改后的类的几点变化：

- 该类现在继承自 `ABC`，这意味着它正式成为了一个抽象基类。
- `headings` 和 `row` 方法都用 `@abstractmethod` 进行了装饰。这告诉 Python，`TableFormatter` 的任何子类都必须实现这些方法。
- 我们用 `pass` 替换了 `NotImplementedError`。`@abstractmethod` 装饰器会确保子类实现这些方法，所以我们不再需要 `NotImplementedError` 了。

## 测试你的抽象基类

现在我们已经将 `TableFormatter` 类变成了一个抽象基类，让我们测试一下它是否能正常工作。我们将创建一个名为 `test_abc.py` 的文件，并包含以下代码：

```python
from tableformat import TableFormatter

# Test case 1: Define a class with a misspelled method
try:
    class NewFormatter(TableFormatter):
        def headers(self, headings):  # Misspelled 'headings'
            pass
        def row(self, rowdata):
            pass

    f = NewFormatter()
    print("Test 1 failed - abstract method enforcement not working")
except TypeError as e:
    print(f"Test 1 passed - caught error: {e}")

# Test case 2: Define a class that properly implements all methods
try:
    class ProperFormatter(TableFormatter):
        def headings(self, headers):
            pass
        def row(self, rowdata):
            pass

    f = ProperFormatter()
    print("Test 2 passed - proper implementation works")
except TypeError as e:
    print(f"Test 2 failed - error: {e}")
```

在这段代码中，我们有两个测试用例。第一个测试用例定义了一个 `NewFormatter` 类，它试图继承自 `TableFormatter`，但方法名拼写错误。第二个测试用例定义了一个 `ProperFormatter` 类，它正确地实现了所有必需的方法。

要运行测试，打开终端并运行以下命令：

```bash
python test_abc.py
```

你应该会看到类似于以下的输出：

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

这个输出确认了我们的抽象基类按预期工作。第一个测试用例失败是因为 `NewFormatter` 类没有正确实现 `headings` 方法。第二个测试用例通过是因为 `ProperFormatter` 类实现了所有必需的方法。
