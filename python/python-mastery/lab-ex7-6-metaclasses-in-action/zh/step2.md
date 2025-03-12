# 收集验证器类型

在 Python 中，验证器（validators）是帮助我们确保数据符合特定标准的类。本实验的首要任务是修改基础的 `Validator` 类，使其能够收集所有的子类。为什么要这么做呢？通过收集所有的验证器子类，我们可以创建一个包含所有验证器类型的命名空间。之后，我们会将这个命名空间注入到 `Structure` 类中，这样就能更轻松地管理和使用不同的验证器。

现在，让我们开始编写代码。打开 `validate.py` 文件。你可以在终端中使用以下命令来打开它：

```bash
code validate.py
```

文件打开后，我们需要为 `Validator` 类添加一个类级别的字典和一个 `__init_subclass__()` 方法。类级别的字典将用于存储所有的验证器子类，而 `__init_subclass__()` 方法是 Python 中的一个特殊方法，每当定义当前类的子类时，它都会被调用。

在 `Validator` 类定义之后，添加以下代码：

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

添加代码后，修改后的 `Validator` 类应该如下所示：

```python
class Validator:
    validators = {}  # Dictionary to collect all validator subclasses

    @classmethod
    def __init_subclass__(cls):
        """Register each validator subclass in the validators dictionary"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

现在，每当定义一个新的验证器类型，如 `String` 或 `PositiveInteger` 时，Python 会自动调用 `__init_subclass__()` 方法。该方法会将新的验证器子类添加到 `validators` 字典中，使用类名作为键。

让我们测试一下代码是否正常工作。我们将创建一个简单的 Python 脚本，检查 `validators` 字典的内容。你可以在终端中运行以下命令：

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

如果一切正常，你应该会看到类似以下的输出，显示所有的验证器类型及其对应的类：

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

现在我们有了一个包含所有验证器类型的字典，接下来就可以用它来创建元类了。
