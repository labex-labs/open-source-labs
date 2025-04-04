# 处理多个股票对象

在面向对象编程中，类就像是一个蓝图，而该类的实例则是基于这个蓝图创建的实际对象。我们的 `Stock` 类是用于表示股票的蓝图。我们可以创建这个 `Stock` 类的多个实例来表示不同的股票。每个实例都有自己的一组属性，例如股票名称、股数和每股价格。

1. 在 Python 交互会话仍在运行的情况下，我们将创建另一个 `Stock` 对象。这次，它将代表 IBM 公司的股票。要创建 `Stock` 类的一个实例，我们像调用函数一样调用类名，并传入必要的参数。这里的参数是股票名称、股数和每股价格。

```python
t = Stock('IBM', 50, 91.5)
```

在这行代码中，我们正在创建一个名为 `t` 的新 `Stock` 对象，它代表 IBM 公司的股票。该股票有 50 股，每股价格为 91.5 美元。

2. 现在，我们要计算这只新股票的成本。`Stock` 类有一个名为 `cost()` 的方法，它通过将股数乘以每股价格来计算股票的总成本。

```python
t.cost()
```

当你运行这段代码时，Python 将在 `t` 对象上调用 `cost()` 方法，并返回总成本。

输出：

```
4575.0
```

3. 我们可以使用 Python 的字符串格式化功能，以一种美观、有条理的方式来格式化和显示我们的股票信息。字符串格式化允许我们指定不同类型的数据在字符串中应该如何呈现。

```python
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
```

在这段代码中，我们使用了 Python 中的旧式字符串格式化。`%` 运算符用于将值替换到字符串模板中。字符串模板 `'%10s %10d %10.2f'` 定义了股票名称、股数和价格应该如何格式化。

输出：

```
      GOOG        100     490.10
```

这个格式化后的字符串的工作原理如下：

- `%10s` 将字符串格式化为宽度为 10 个字符的字段（右对齐）。这意味着股票名称将被放置在一个宽度为 10 个字符的空间中，并且在该空间内右对齐。
- `%10d` 将整数格式化为宽度为 10 个字符的字段。因此，股数将被放置在一个宽度为 10 个字符的空间中。
- `%10.2f` 将浮点数格式化为保留两位小数、宽度为 10 个字符的字段。价格将显示为两位小数，并放置在一个宽度为 10 个字符的空间中。

4. 现在，让我们以同样的方式格式化 IBM 股票的信息。我们只需要在字符串格式化代码中将对象名称从 `s` 替换为 `t`。

```python
print('%10s %10d %10.2f' % (t.name, t.shares, t.price))
```

输出：

```
       IBM         50      91.50
```

5. 在现代 Python 中，我们还可以使用 f - 字符串进行格式化。f - 字符串更易读且更易于使用。让我们使用 f - 字符串来比较这两只股票的成本。

```python
print(f"Google stock costs ${s.cost()}, IBM stock costs ${t.cost()}")
```

在这个 f - 字符串中，我们直接将表达式嵌入到花括号 `{}` 中。Python 将计算这些表达式，并将结果插入到字符串中。

输出：

```
Google stock costs $49010.0, IBM stock costs $4575.0
```

6. 当你完成实验后，是时候退出 Python 交互模式了。你可以使用 `exit()` 函数来实现这一点。

```python
exit()
```

每个 `Stock` 对象都维护着自己的一组属性，这展示了面向对象编程中类实例的工作方式。这使我们能够创建多个股票对象，每个对象具有不同的值，同时共享相同的方法。
