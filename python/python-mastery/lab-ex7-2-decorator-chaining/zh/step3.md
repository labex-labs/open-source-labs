# 将装饰器应用于类方法

现在，我们将探讨装饰器如何与类方法进行交互。这可能有点棘手，因为 Python 有不同类型的方法：实例方法、类方法、静态方法和属性方法。装饰器是一种函数，它接受另一个函数并扩展该函数的行为，而无需显式修改它。当将装饰器应用于类方法时，我们需要注意它们如何与这些不同类型的方法协同工作。

## 理解挑战

让我们看看将 `@logged` 装饰器应用于不同类型的方法时会发生什么。`@logged` 装饰器可能用于记录方法调用的信息。

1. 在 WebIDE 中创建一个新文件 `methods.py`。这个文件将包含一个类，其中不同类型的方法都使用 `@logged` 装饰器进行装饰。

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

在这段代码中，我们有一个名为 `Spam` 的类，它包含四种不同类型的方法。每个方法都使用 `@logged` 装饰器进行装饰，有些方法还使用了其他内置装饰器，如 `@classmethod`、`@staticmethod` 和 `@property`。

2. 让我们测试一下它的工作情况。我们将在终端中运行一个 Python 命令来调用这些方法并查看输出。

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

当你运行这个命令时，你可能会注意到一些问题：

- `@property` 装饰器与 `@logged` 装饰器可能无法正确协同工作。`@property` 装饰器用于将方法定义为属性，它有特定的工作方式。当与 `@logged` 装饰器结合使用时，可能会产生冲突。
- 对于 `@classmethod` 和 `@staticmethod`，装饰器的顺序很重要。装饰器的应用顺序会改变方法的行为。

## 装饰器的顺序

当你应用多个装饰器时，它们是从下到上依次应用的。这意味着离方法定义最近的装饰器最先应用，然后上面的装饰器按顺序依次应用。例如：

```python
@decorator1
@decorator2
def func():
    pass
```

这相当于：

```python
func = decorator1(decorator2(func))
```

在这个例子中，`decorator2` 首先应用于 `func`，然后 `decorator1` 应用于 `decorator2(func)` 的结果。

## 修正装饰器顺序

让我们更新 `methods.py` 文件来修正装饰器的顺序。通过改变装饰器的顺序，我们可以确保每个方法都能按预期工作。

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

在这个更新后的版本中：

- 对于 `instance_method`，顺序无关紧要。实例方法是在类的实例上调用的，`@logged` 装饰器可以以任何顺序应用，而不会影响其基本功能。
- 对于 `class_method`，我们在 `@logged` 之后应用 `@classmethod`。`@classmethod` 装饰器会改变方法的调用方式，在 `@logged` 之后应用它可以确保日志记录正常工作。
- 对于 `static_method`，我们在 `@logged` 之后应用 `@staticmethod`。与 `@classmethod` 类似，`@staticmethod` 装饰器有其自身的行为，与 `@logged` 装饰器的顺序需要正确。
- 对于 `property_method`，我们在 `@logged` 之后应用 `@property`。这可以确保在获得日志记录功能的同时，保持属性的行为。

3. 让我们测试更新后的代码。我们将运行与之前相同的命令，看看问题是否得到解决。

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

现在你应该会看到所有方法类型都有正确的日志记录：

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## 方法装饰器的最佳实践

在使用方法装饰器时，请遵循以下最佳实践：

1. 在自定义装饰器之后应用方法转换装饰器（`@classmethod`、`@staticmethod`、`@property`）。这可以确保自定义装饰器首先执行其日志记录或其他操作，然后内置装饰器可以按预期转换方法。
2. 要注意装饰器的执行是在类定义时发生的，而不是在方法调用时。这意味着装饰器中的任何设置或初始化代码将在类定义时运行，而不是在方法调用时。
3. 对于更复杂的情况，你可能需要为不同的方法类型创建专门的装饰器。不同类型的方法有不同的行为，一刀切的装饰器可能并不适用于所有情况。
