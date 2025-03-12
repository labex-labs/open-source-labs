# 探索元类继承

元类有一个很有趣的特性：它们具有“粘性”。这意味着一旦一个类使用了某个元类，其继承层次结构中的所有子类也将使用同一个元类。换句话说，元类属性会沿着继承链传播。

让我们来实际看看这种情况：

1. 首先，打开 `mymeta.py` 文件。在这个文件的末尾，我们要添加一个新类。这个名为 `MyStock` 的类将继承自 `Stock` 类。`__init__` 方法用于初始化对象的属性，我们使用 `super().__init__` 调用父类的 `__init__` 方法来初始化公共属性。`info` 方法用于返回一个包含股票信息的格式化字符串。添加以下代码：

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2. 添加代码后，保存 `mymeta.py` 文件。保存文件可确保我们所做的更改被保存，并且稍后可以使用。

3. 现在，我们将创建一个名为 `test_inheritance.py` 的新文件，以测试元类的继承行为。在这个文件中，我们将从 `mymeta.py` 文件中导入 `MyStock` 类。然后，我们将创建一个 `MyStock` 类的实例，调用其方法，并打印结果，以查看元类如何通过继承发挥作用。在 `test_inheritance.py` 中添加以下代码：

```python
# test_inheritance.py
from mymeta import MyStock

# Create a MyStock instance
tech_stock = MyStock("MSFT", 50, 305.75, "Technology")

# Test the methods
print(tech_stock.info())
print(f"Total cost: ${tech_stock.cost()}")

# Sell some shares
tech_stock.sell(5)
print(f"After selling: {tech_stock.shares} shares remaining")
print(f"Updated cost: ${tech_stock.cost()}")
```

4. 最后，运行 `test_inheritance.py` 文件，看看元类如何通过继承发挥作用。打开终端，导航到 `test_inheritance.py` 文件所在的目录，然后运行以下命令：

```bash
python3 test_inheritance.py
```

你应该会看到类似以下的输出：

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Creating class : MyStock
Base classes   : (<class 'mymeta.Stock'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'info', '__doc__']
MSFT (Technology): 50 shares at $305.75
Total cost: $15287.5
After selling: 45 shares remaining
Updated cost: $13758.75
```

注意，即使我们没有为 `MyStock` 类显式指定元类，元类仍然会被应用。这清楚地展示了元类如何通过继承传播。

## 元类的实际应用

在我们的示例中，元类只是打印类的信息。然而，元类在实际编程中有很多实际应用：

1. **验证**：你可以使用元类来检查一个类是否具有所需的方法或属性。这有助于确保类在使用前满足某些标准。
2. **注册**：元类可以自动将类注册到一个注册表中。当你需要跟踪某种类型的所有类时，这很有用。
3. **接口强制**：它们可用于确保类实现所需的接口。这有助于在代码中保持一致的结构。
4. **面向切面编程**：元类可以为方法添加行为。例如，你可以在不直接修改方法代码的情况下，为方法添加日志记录或性能监控功能。
5. **ORM 系统**：在像 Django 或 SQLAlchemy 这样的对象关系映射（ORM）系统中，元类用于将类映射到数据库表。这简化了应用程序中的数据库操作。

元类非常强大，但应该谨慎使用。正如著名的《Python 之禅》作者 Tim Peters 所说：“元类是比 99% 的用户应该担心的更深层次的魔法。”
