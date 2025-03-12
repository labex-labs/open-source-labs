# 使用描述符实现类型检查

在这一步中，我们将创建一个使用描述符进行类型检查的 `Stock` 类。但首先，让我们了解一下什么是描述符。描述符是 Python 中非常强大的特性，它能让你控制类中属性的访问方式。

描述符是定义了如何在其他对象上访问属性的对象。它们通过实现 `__get__`、`__set__` 和 `__delete__` 等特殊方法来实现这一点。这些方法使描述符能够管理属性的获取、设置和删除。描述符在实现验证、类型检查和计算属性方面非常有用。例如，你可以使用描述符确保某个属性始终是正数或特定格式的字符串。

`validate.py` 文件中已经有验证器类（`String`、`PositiveInteger`、`PositiveFloat`）。我们可以使用这些类来验证 `Stock` 类的属性。

现在，让我们使用描述符创建 `Stock` 类。

1. 首先，在编辑器中打开 `stock.py` 文件。你可以在终端中运行以下命令来完成此操作：

```bash
code ~/project/stock.py
```

此命令使用 `code` 编辑器打开位于 `~/project` 目录下的 `stock.py` 文件。

2. 文件打开后，将占位内容替换为以下代码：

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Create an __init__ method based on _fields
Stock.create_init()
```

让我们来分析一下这段代码的作用。`_fields` 元组定义了 `Stock` 类的属性，这些是 `Stock` 对象将具有的属性名称。

`name`、`shares` 和 `price` 属性被定义为描述符对象。`String()` 描述符确保 `name` 属性是字符串；`PositiveInteger()` 描述符确保 `shares` 属性是正整数；`PositiveFloat()` 描述符确保 `price` 属性是正浮点数。

`cost` 属性是一个计算属性，它根据股票数量和每股价格计算股票的总成本。

`sell` 方法用于减少股票数量。当你调用此方法并传入要出售的股票数量时，它会从 `shares` 属性中减去该数量。

`Stock.create_init()` 行动态地为我们的类创建一个 `__init__` 方法。这个方法允许我们通过传入 `name`、`shares` 和 `price` 属性的值来创建 `Stock` 对象。

3. 添加代码后，保存文件。这将确保你的更改被保存，并且在运行测试时可以使用。

4. 现在，让我们运行测试来验证你的实现。首先，通过运行以下命令将目录更改为 `~/project` 目录：

```bash
cd ~/project
```

然后，使用以下命令运行测试：

```bash
python3 teststock.py
```

如果你的实现正确，你应该会看到类似于以下的输出：

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

这个输出意味着所有测试都通过了，描述符成功验证了每个属性的类型！

让我们尝试在 Python 解释器中创建一个 `Stock` 对象。首先，确保你位于 `~/project` 目录中。然后，运行以下命令：

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

你应该会看到以下输出：

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

你已经成功实现了用于类型检查的描述符！现在，让我们进一步改进这段代码。
