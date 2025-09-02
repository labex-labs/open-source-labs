# 添加方法参数验证

在 Python 中，验证数据是编写健壮代码的重要组成部分。在本节中，我们将通过自动验证方法参数来进一步提升我们的验证能力。`validate.py` 文件已经包含了一个 `@validated` 装饰器。Python 中的装饰器是一种可以修改另一个函数的特殊函数。这里的 `@validated` 装饰器可以根据其注解检查函数参数。Python 中的注解是一种为函数参数和返回值添加元数据的方式。

让我们修改代码以将此装饰器应用于带有注解的方法：

1. 首先，我们需要了解 `validated` 装饰器的工作原理。在你的编辑器中打开 `validate.py` 文件进行查看。

`validated` 装饰器使用函数注解来验证参数。在允许函数运行之前，它会为每个注解的参数创建一个验证器类的实例，并调用 `validate` 方法来检查参数。例如，如果一个参数被注解为 `PositiveInteger`，装饰器将创建一个 `PositiveInteger` 实例并验证传入的值确实是一个正整数。如果验证失败，它会收集所有错误并引发一个带有详细错误消息的 `TypeError`。

2. 现在，我们将修改 `structure.py` 中的 `validate_attributes` 函数，以使用 `validated` 装饰器包装带有注解的方法。这意味着类中任何带有注解的方法都将自动验证其参数。在你的编辑器中打开 `structure.py` 文件。

3. 更新 `validate_attributes` 函数：

```python
def validate_attributes(cls):
    """
    Class decorator that:
    1. Extracts Validator instances and builds _fields and _types lists
    2. Applies @validated decorator to methods with annotations
    """
    # Import the validated decorator
    from validate import validated

    # Process validator descriptors
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Apply @validated decorator to methods with annotations
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # Create initialization method
    cls.create_init()

    return cls
```

这个更新后的函数现在执行以下操作：

1. 它像以前一样处理验证器描述符。验证器描述符用于为类属性定义验证规则。
2. 它在类中查找所有带有注解的方法。注解被添加到方法参数中，以指定参数的预期类型。
3. 它将 `@validated` 装饰器应用于这些方法。这确保了传递给这些方法的参数会根据其注解进行验证。

4. 进行这些更改后保存文件。保存文件很重要，因为它确保了我们的修改被存储并且以后可以使用。

5. 现在，让我们更新 `Stock` 类中的 `sell` 方法以包含注解。注解有助于指定参数的预期类型，这将由 `@validated` 装饰器用于验证。在你的编辑器中打开 `stock.py` 文件。

6. 修改 `sell` 方法以包含类型注解：

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

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

重要的更改是将 `: PositiveInteger` 添加到 `nshares` 参数。这告诉 Python（以及我们的 `@validated` 装饰器）使用 `PositiveInteger` 验证器来验证此参数。因此，当我们调用 `sell` 方法时，`nshares` 参数必须是一个正整数。

7. 再次运行测试以验证一切是否仍然正常工作。运行测试是确保我们的更改没有破坏任何现有功能的好方法。

```bash
cd ~/project
python3 teststock.py
```

你应该会看到所有测试都通过：

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

8. 让我们测试我们新的参数验证。我们将尝试使用有效和无效参数调用 `sell` 方法，以查看验证是否按预期工作。

```bash
cd ~/project
python3 -c "
from stock import Stock
s = Stock('GOOG', 100, 490.1)
s.sell(25)
print(s)
try:
    s.sell(-25)
except Exception as e:
    print(f'Error: {e}')
"
```

你应该会看到类似以下的输出：

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: nshares must be >= 0
```

这表明我们的方法参数验证正在起作用！第一次调用 `sell(25)` 成功，因为 `25` 是一个正整数。但第二次调用 `sell(-25)` 失败，因为 `-25` 不是一个正整数。

你现在已经实现了一个完整的系统，用于：

1. 使用描述符验证类属性。描述符用于为类属性定义验证规则。
2. 使用类装饰器自动收集字段信息。类装饰器可以修改类的行为，例如收集字段信息。
3. 将行数据转换为实例。这在处理来自外部源的数据时很有用。
4. 使用注解验证方法参数。注解有助于为验证指定参数的预期类型。

这展示了在 Python 中结合使用描述符和装饰器来创建富有表现力、自我验证的类的强大功能。
