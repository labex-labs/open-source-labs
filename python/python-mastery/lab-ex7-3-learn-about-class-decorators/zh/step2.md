# 创建用于验证的类装饰器

在上一步中，我们的实现是可行的，但存在冗余。我们必须同时指定 `_fields` 元组和描述符属性，这不是很高效，我们可以对其进行改进。在 Python 中，类装饰器是一个强大的工具，可以帮助我们简化这个过程。类装饰器是一个函数，它接受一个类作为参数，以某种方式对其进行修改，然后返回修改后的类。通过使用类装饰器，我们可以自动从描述符中提取字段信息，这将使我们的代码更简洁、更易于维护。

让我们创建一个类装饰器来简化我们的代码。你需要按照以下步骤操作：

1. 首先，打开 `structure.py` 文件。你可以在终端中使用以下命令：

```bash
code ~/project/structure.py
```

此命令将在你的代码编辑器中打开 `structure.py` 文件。

2. 接下来，在 `structure.py` 文件的顶部，紧接在任何导入语句之后添加以下代码。这段代码定义了我们的类装饰器：

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

让我们来分析一下这个装饰器的作用：

- 它首先创建一个名为 `validators` 的空列表。然后，使用 `vars(cls).items()` 遍历类的所有属性。如果某个属性是 `Validator` 类的实例，则将该属性添加到 `validators` 列表中。
- 之后，它设置类的 `_fields` 属性。它从 `validators` 列表中的验证器创建一个名称列表，并将其赋值给 `cls._fields`。
- 最后，它调用类的 `create_init()` 方法来生成 `__init__` 方法，然后返回修改后的类。

3. 添加代码后，保存 `structure.py` 文件。保存文件可确保你的更改得以保留。

4. 现在，我们需要修改 `stock.py` 文件以使用这个新的装饰器。使用以下命令打开 `stock.py` 文件：

```bash
code ~/project/stock.py
```

5. 更新 `stock.py` 文件以使用 `validate_attributes` 装饰器。将现有代码替换为以下内容：

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

注意我们所做的更改：

- 我们在 `Stock` 类定义的正上方添加了 `@validate_attributes` 装饰器，这告诉 Python 将 `validate_attributes` 装饰器应用于 `Stock` 类。
- 我们移除了显式的 `_fields` 声明，因为装饰器会自动处理它。
- 我们还移除了对 `Stock.create_init()` 的调用，因为装饰器会负责创建 `__init__` 方法。

结果是，类现在变得更简单、更简洁了。装饰器处理了我们以前手动处理的所有细节。

6. 进行这些更改后，我们需要验证一切是否仍按预期工作。再次使用以下命令运行测试：

```bash
cd ~/project
python3 teststock.py
```

如果一切正常，你应该会看到以下输出：

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

这个输出表明所有测试都已成功通过。

让我们也交互式地测试一下我们的 `Stock` 类。在终端中运行以下命令：

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

你应该会看到以下输出：

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

太棒了！你已经成功实现了一个类装饰器，它通过自动处理字段声明和初始化来简化我们的代码。这使我们的代码更高效、更易于维护。
