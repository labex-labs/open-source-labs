# 测试我们的实现

现在我们已经实现了元类并修改了 `Structure` 类，是时候测试我们的实现了。测试至关重要，因为它能帮助我们确保一切正常运行。通过运行测试，我们可以尽早发现潜在问题，并确保代码按预期工作。

首先，让我们运行单元测试，看看 `Stock` 类是否按预期工作。单元测试是小型的、独立的测试，用于检查代码的各个部分。在这种情况下，我们要确保 `Stock` 类功能正常。要运行单元测试，你可以在终端中使用以下命令：

```bash
python3 teststock.py
```

如果一切正常，所有测试都应该顺利通过，没有错误。当测试成功运行时，输出应该类似于以下内容：

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

这些点代表每个通过的测试，最后的 `OK` 表示所有测试都成功了。

现在，让我们用一些实际数据和表格格式化功能来测试 `Stock` 类。这将为我们提供一个更接近真实场景的测试，让我们了解 `Stock` 类如何与数据交互，以及表格格式化功能如何工作。你可以在终端中使用以下命令：

```bash
python3 -c "
from stock import Stock
from reader import read_csv_as_instances
from tableformat import create_formatter, print_table

# Read portfolio data into Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print('Portfolio:')
print(portfolio)

# Format and print the portfolio data
print('\nFormatted table:')
formatter = create_formatter('text')
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

在这段代码中，我们首先导入必要的类和函数。然后将 CSV 文件中的数据读取到 `Stock` 实例中。接着，我们打印投资组合数据，再将其格式化为表格并打印出来。

你应该会看到类似以下的输出：

```
Portfolio:
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]

Formatted table:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

花点时间来欣赏一下我们所取得的成果：

1. 我们创建了一种机制来自动收集所有验证器类型。这意味着我们无需手动跟踪所有验证器，节省了时间并降低了出错的可能性。
2. 我们实现了一个元类，将这些类型注入到 `Structure` 子类的命名空间中。这使得子类可以使用这些验证器，而无需显式导入它们。
3. 我们消除了对验证器类型的显式导入需求。这使我们的代码更简洁、易读。
4. 所有这些操作都在幕后完成，使得定义新结构的代码简洁明了。

最终的 `stock.py` 文件与没有使用元类时相比，显得格外简洁：

```python
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

无需直接导入验证器类型，代码更加简洁，也更易于维护。这是元类如何提高代码质量的一个很好的例子。
