# 理解 Python 中的绑定方法

在 Python 中，方法是一种特殊类型的属性，你可以调用它们。当你通过对象访问方法时，你得到的是所谓的“绑定方法”。绑定方法本质上是与特定对象绑定的方法。这意味着它可以访问对象的数据并对其进行操作。

## 将方法作为属性访问

让我们使用 `Stock` 类开始探索绑定方法。首先，我们将了解如何将方法作为对象的属性进行访问。

```python
# Open a Python interactive shell
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Access the cost method without calling it
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# You can also do this in one step
print(s.cost())  # Output: 49010.0
```

在上面的代码中，我们首先导入 `Stock` 类并创建一个实例。然后，我们在不实际调用的情况下访问 `s` 对象的 `cost` 方法。这会得到一个绑定方法。当我们调用这个绑定方法时，它会根据对象的数据计算成本。你也可以一步直接在对象上调用该方法。

## 使用 `getattr()` 访问方法

另一种访问方法的方式是使用 `getattr()` 函数。这个函数允许你通过名称获取对象的属性。

```python
# Get the cost method using getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# Get and call in one step
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

在这里，我们使用 `getattr()` 从 `s` 对象获取 `cost` 方法。和之前一样，我们可以调用绑定方法来获取结果。你甚至可以在一行代码中完成获取和调用方法的操作。

## 绑定方法及其对象

绑定方法始终会保留对其所属对象的引用。这意味着即使你将方法存储在变量中，它仍然知道自己属于哪个对象，并可以访问该对象的数据。

```python
# Store the cost method in a variable
c = s.cost

# Call the method
print(c())  # Output: 49010.0

# Change the object's state
s.shares = 75

# Call the method again - it sees the updated state
print(c())  # Output: 36757.5
```

在这个例子中，我们将 `cost` 方法存储在变量 `c` 中。当我们调用 `c()` 时，它会根据对象的当前数据计算成本。然后，我们更改 `s` 对象的 `shares` 属性。当我们再次调用 `c()` 时，它会使用更新后的数据计算新的成本。

## 探索绑定方法的内部结构

绑定方法有两个重要的属性，它们能为我们提供更多关于该方法的信息。

- `__self__`：这个属性引用方法所绑定的对象。
- `__func__`：这个属性是表示该方法的实际函数对象。

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

在这里，我们访问绑定方法 `c` 的 `__self__` 和 `__func__` 属性。我们可以看到，`__self__` 是 `s` 对象，而 `__func__` 是 `cost` 函数。我们甚至可以通过将对象作为参数传递来手动调用该函数，其结果与直接调用绑定方法相同。

## 带参数方法的示例

让我们看看绑定方法如何与带参数的方法（如 `sell()` 方法）一起工作。

```python
# Get the sell method
sell_method = s.sell

# Examine the method
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Call the method with an argument
sell_method(25)
print(s.shares)  # Output: 50

# Call the method manually using __func__ and __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

在这个例子中，我们将 `sell` 方法作为绑定方法获取。当我们使用参数调用它时，它会更新 `s` 对象的 `shares` 属性。我们也可以使用 `__func__` 和 `__self__` 属性手动调用该方法，并传递参数。

理解绑定方法有助于你深入了解 Python 对象系统的工作原理，这对于调试、元编程和创建高级编程模式非常有用。
