# 创建算法模板类

在这一步中，我们将使用抽象基类来实现模板方法模式。目标是减少 CSV 解析功能中的代码重复。代码重复会使你的代码更难维护和更新。通过使用模板方法模式，我们可以为 CSV 解析代码创建一个通用结构，并让子类处理具体细节。

## 理解模板方法模式

模板方法模式是一种行为设计模式。它就像是算法的蓝图。在一个方法中，它定义了算法的整体结构或“骨架”。然而，它并不完全实现所有步骤。相反，它将一些步骤推迟到子类中实现。这意味着子类可以重新定义算法的某些部分，而不改变其整体结构。

在我们的例子中，如果你查看 `reader.py` 文件，你会注意到 `read_csv_as_dicts()` 和 `read_csv_as_instances()` 函数有很多相似的代码。它们之间的主要区别在于如何从 CSV 文件的行中创建记录。通过使用模板方法模式，我们可以避免多次编写相同的代码。

## 添加 `CSVParser` 基类

让我们从为 CSV 解析添加一个抽象基类开始。打开 `reader.py` 文件。我们将在文件顶部，紧接在导入语句之后添加 `CSVParser` 抽象基类。

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

这个 `CSVParser` 类作为 CSV 解析的模板。`parse` 方法包含了读取 CSV 文件的常见步骤，如打开文件、获取表头以及遍历行。从行中创建记录的具体逻辑被抽象到 `make_record()` 方法中。由于它是一个抽象方法，任何继承自 `CSVParser` 的类都必须实现这个方法。

## 实现具体的解析器类

现在我们有了基类，我们需要创建具体的解析器类。这些类将实现具体的记录创建逻辑。

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

`DictCSVParser` 类用于将记录创建为字典。它在构造函数中接受一个类型列表。`make_record` 方法使用这些类型来转换行中的值并创建一个字典。

`InstanceCSVParser` 类用于将记录创建为类的实例。它在构造函数中接受一个类。`make_record` 方法调用该类的 `from_row` 方法从行中创建一个实例。

## 重构原始函数

现在，让我们重构原始的 `read_csv_as_dicts()` 和 `read_csv_as_instances()` 函数以使用这些新类。

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

这些重构后的函数与原始函数具有相同的接口。但在内部，它们使用了我们刚刚创建的新解析器类。这样，我们就将通用的 CSV 解析逻辑与具体的记录创建逻辑分离开来。

## 测试你的实现

让我们检查一下我们重构后的代码是否能正常工作。创建一个名为 `test_reader.py` 的文件，并在其中添加以下代码。

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

要运行测试，打开终端并执行以下命令：

```bash
python test_reader.py
```

你应该会看到类似于以下的输出：

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

如果你看到这个输出，这意味着你重构后的代码能正常工作。原始函数和直接使用解析器都产生了预期的结果。
