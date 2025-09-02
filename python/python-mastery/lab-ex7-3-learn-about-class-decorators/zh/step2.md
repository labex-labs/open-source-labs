# 创建用于验证的类装饰器

在上一个步骤中，我们的实现是有效的，但存在冗余。我们必须同时指定 `_fields` 元组和描述器属性。这效率不高，我们可以进行改进。在 Python 中，类装饰器是一个强大的工具，可以帮助我们简化这个过程。类装饰器是一个函数，它接收一个类作为参数，对其进行某种修改，然后返回修改后的类。通过使用类装饰器，我们可以自动从描述器中提取字段信息，这将使我们的代码更简洁、更易于维护。

让我们创建一个类装饰器来简化我们的代码。以下是你需要遵循的步骤：

1. 首先，在你的编辑器中打开 `structure.py` 文件。

2. 接下来，在 `structure.py` 文件的顶部，紧随任何导入语句之后，添加以下代码。这段代码定义了我们的类装饰器：

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

让我们来分析一下这个装饰器做了什么：

- 它首先创建一个名为 `validators` 的空列表。然后，它使用 `vars(cls).items()` 遍历类的所有属性。如果某个属性是 `Validator` 类的实例，它就会将该属性添加到 `validators` 列表中。
- 之后，它设置类的 `_fields` 属性。它从 `validators` 列表中的验证器创建名称列表，并将其赋值给 `cls._fields`。
- 最后，它调用类的 `create_init()` 方法来生成 `__init__` 方法，然后返回修改后的类。

3. 添加代码后，保存 `structure.py` 文件。保存文件可确保你的更改得以保留。

4. 现在，我们需要修改 `stock.py` 文件以使用这个新的装饰器。在你的编辑器中打开 `stock.py` 文件。

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

请注意我们所做的更改：

- 我们在 `Stock` 类定义上方添加了 `@validate_attributes` 装饰器。这告诉 Python 将 `validate_attributes` 装饰器应用于 `Stock` 类。
- 我们删除了显式的 `_fields` 声明，因为装饰器将自动处理它。
- 我们还删除了对 `Stock.create_init()` 的调用，因为装饰器负责创建 `__init__` 方法。

因此，该类现在更简单、更简洁了。装饰器处理了我们以前手动处理的所有细节。

6. 进行这些更改后，我们需要验证一切是否仍按预期工作。使用以下命令再次运行测试：

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

此输出表明所有测试都已成功通过。

让我们也在交互式环境中测试我们的 `Stock` 类。在终端中运行以下命令：

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

你应该会看到以下输出：

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

太棒了！你已成功实现了一个类装饰器，该装饰器通过自动处理字段声明和初始化来简化我们的代码。这使得我们的代码更高效、更易于维护。
