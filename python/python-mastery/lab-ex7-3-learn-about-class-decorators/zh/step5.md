# 添加方法参数验证

在 Python 中，数据验证是编写健壮代码的重要部分。在本节中，我们将进一步扩展验证功能，实现方法参数的自动验证。`validate.py` 文件中已经包含了一个 `@validated` 装饰器。在 Python 中，装饰器是一种特殊的函数，它可以修改其他函数。这里的 `@validated` 装饰器可以根据函数参数的注解来检查参数。Python 中的注解是一种为函数参数和返回值添加元数据的方式。

让我们修改代码，将这个装饰器应用到带有注解的方法上：

1. 首先，你需要了解 `validated` 装饰器的工作原理。打开 `validate.py` 文件进行查看：

```bash
code ~/project/validate.py
```

`validated` 装饰器使用函数注解来验证参数。在允许函数运行之前，它会根据注解类型检查每个参数。例如，如果一个参数被注解为整数，装饰器会确保传入的值确实是整数。

2. 现在，我们将修改 `structure.py` 中的 `validate_attributes` 函数，用 `validated` 装饰器包装带有注解的方法。这意味着类中任何带有注解的方法，其参数都会被自动验证。打开 `structure.py` 文件：

```bash
code ~/project/structure.py
```

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

1. 像之前一样处理验证器描述符。验证器描述符用于定义类属性的验证规则。
2. 找出类中所有带有注解的方法。注解被添加到方法参数中，用于指定参数的预期类型。
3. 将 `@validated` 装饰器应用到这些方法上。这确保了传递给这些方法的参数会根据其注解进行验证。

4. 完成这些更改后保存文件。保存文件很重要，因为这样可以确保我们的修改被保存下来，以便后续使用。

5. 现在，让我们更新 `Stock` 类中的 `sell` 方法，为其添加注解。注解有助于指定参数的预期类型，`@validated` 装饰器将使用这些注解进行验证。打开 `stock.py` 文件：

```bash
code ~/project/stock.py
```

6. 修改 `sell` 方法，添加类型注解：

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

重要的更改是在 `nshares` 参数后添加了 `: PositiveInteger`。这告诉 Python（以及我们的 `@validated` 装饰器）使用 `PositiveInteger` 验证器来验证这个参数。因此，当我们调用 `sell` 方法时，`nshares` 参数必须是正整数。

7. 再次运行测试，验证一切仍然正常工作。运行测试是确保我们的更改没有破坏现有功能的好方法。

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

8. 让我们测试新的参数验证功能。我们将尝试使用有效和无效的参数调用 `sell` 方法，看看验证是否按预期工作。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); s.sell(25); print(s); try: s.sell(-25); except Exception as e: print(f'Error: {e}')"
```

你应该会看到类似以下的输出：

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: must be >= 0
```

这表明我们的方法参数验证功能正常工作！第一次调用 `sell(25)` 成功，因为 `25` 是正整数。但第二次调用 `sell(-25)` 失败，因为 `-25` 不是正整数。

你现在已经实现了一个完整的系统，用于：

1. 使用描述符验证类属性。描述符用于定义类属性的验证规则。
2. 使用类装饰器自动收集字段信息。类装饰器可以修改类的行为，例如收集字段信息。
3. 将行数据转换为实例。这在处理来自外部源的数据时非常有用。
4. 使用注解验证方法参数。注解有助于指定用于验证的参数的预期类型。

这展示了在 Python 中结合使用描述符和装饰器来创建具有表现力、自验证类的强大功能。
