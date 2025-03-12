# 委托：继承的替代方案

在面向对象编程中，代码的复用和扩展是常见的任务。实现这一目标主要有两种方式：继承和委托。

**继承** 是一种机制，通过它子类可以从父类继承方法和属性。子类可以选择重写部分继承的方法，以提供自己的实现。

**委托** 则是指一个对象包含另一个对象，并将特定的方法调用转发给它。

在这一步中，我们将探索委托作为继承的替代方案。我们将实现一个类，将其部分行为委托给另一个对象。

## 建立委托示例

首先，我们需要建立一个基类，供委托类与之交互。

1. 在 `/home/labex/project` 目录下创建一个名为 `base_class.py` 的新文件。该文件将定义一个名为 `Spam` 的类，它有三个方法：`method_a`、`method_b` 和 `method_c`。每个方法都会打印一条消息并返回一个结果。以下是要放入 `base_class.py` 的代码：

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

接下来，我们将创建委托类。

2. 创建一个名为 `delegator.py` 的新文件。在这个文件中，我们将定义一个名为 `DelegatingSpam` 的类，它将部分行为委托给 `Spam` 类的一个实例。

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

在 `__init__` 方法中，我们创建了一个 `Spam` 类的实例。`method_a` 方法重写了原方法，但也调用了 `Spam` 类的 `method_a`。`method_c` 方法则完全重写了原方法。`__getattr__` 是 Python 中的一个特殊方法，当访问 `DelegatingSpam` 类中不存在的属性或方法时会调用它，然后将调用委托给 `Spam` 实例。

现在，让我们创建一个测试文件来验证我们的实现。

3. 创建一个名为 `test_delegation.py` 的测试文件。该文件将创建一个 `DelegatingSpam` 类的实例并调用其方法。

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

最后，我们将运行测试脚本。

4. 在终端中使用以下命令运行测试脚本：

```bash
cd /home/labex/project
python3 test_delegation.py
```

你应该会看到类似于以下的输出：

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## 委托与继承的比较

现在，让我们将委托与传统的继承进行比较。

1. 创建一个名为 `inheritance_example.py` 的文件。在这个文件中，我们将定义一个名为 `InheritingSpam` 的类，它继承自 `Spam` 类。

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

`InheritingSpam` 类重写了 `method_a` 和 `method_c` 方法。在 `method_a` 方法中，我们使用 `super()` 来调用父类的 `method_a`。

接下来，我们将为继承示例创建一个测试文件。

2. 创建一个名为 `test_inheritance.py` 的测试文件。该文件将创建一个 `InheritingSpam` 类的实例并调用其方法。

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

最后，我们将运行继承测试。

3. 在终端中使用以下命令运行继承测试：

```bash
cd /home/labex/project
python3 test_inheritance.py
```

你应该会看到类似于以下的输出：

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## 关键差异与注意事项

让我们来看看委托和继承之间的异同。

1. **方法重写**：委托和继承都允许你重写方法，但语法不同。

   - 在委托中，你定义自己的方法，并决定是否调用被包装对象的方法。
   - 在继承中，你定义自己的方法，并使用 `super()` 来调用父类的方法。

2. **方法访问**：

   - 在委托中，未定义的方法通过 `__getattr__` 方法转发。
   - 在继承中，未定义的方法会自动继承。

3. **类型关系**：

   - 使用委托时，`isinstance(delegating_spam, Spam)` 返回 `False`，因为 `DelegatingSpam` 对象不是 `Spam` 类的实例。
   - 使用继承时，`isinstance(inheriting_spam, Spam)` 返回 `True`，因为 `InheritingSpam` 类继承自 `Spam` 类。

4. **局限性**：通过 `__getattr__` 进行的委托不适用于像 `__getitem__`、`__len__` 等特殊方法。这些方法需要在委托类中显式定义。

委托在以下情况下特别有用：

- 你想自定义对象的行为，而不影响其层次结构。
- 你想组合多个没有共同父类的对象的行为。
- 你需要比继承更多的灵活性。

继承通常在以下情况下更受青睐：

- “是一个”（is-a）关系很明确（例如，汽车是一种交通工具）。
- 你需要在代码中保持类型兼容性。
- 需要继承特殊方法。
