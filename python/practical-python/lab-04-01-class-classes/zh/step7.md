# 练习4.1：将对象用作数据结构

在第2节和第3节中，我们处理了用元组和字典表示的数据。例如，一只股票的持仓可以用这样的元组表示：

```python
s = ('GOOG',100,490.10)
```

或者用这样的字典表示：

```python
s = { 'name'   : 'GOOG',
    'shares' : 100,
     'price'  : 490.10
}
```

你甚至可以编写用于操作此类数据的函数。例如：

```python
def cost(s):
    return s['shares'] * s['price']
```

然而，随着你的程序变得庞大，你可能希望创建一种更好的组织感。因此，另一种表示数据的方法是定义一个类。创建一个名为 `stock.py` 的文件，并定义一个表示单只股票持仓的类 `Stock`。让 `Stock` 的实例具有 `name`、`shares` 和 `price` 属性。例如：

```python
>>> import stock
>>> a = stock.Stock('GOOG',100,490.10)
>>> a.name
'GOOG'
>>> a.shares
100
>>> a.price
490.1
>>>
```

创建更多的 `Stock` 对象并对它们进行操作。例如：

```python
>>> b = stock.Stock('AAPL', 50, 122.34)
>>> c = stock.Stock('IBM', 75, 91.75)
>>> b.shares * b.price
6117.0
>>> c.shares * c.price
6881.25
>>> stocks = [a, b, c]
>>> stocks
[<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>, <stock.Stock object at 0x37d050>]
>>> for s in stocks:
     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

...查看输出...
>>>
```

这里要强调的一点是，类 `Stock` 的作用就像是一个用于创建对象实例的工厂。基本上，你将它当作函数调用，它就会为你创建一个新对象。同样必须强调的是，每个对象都是不同的——它们各自拥有与已创建的其他对象分开的自己的数据。

由类定义的对象在某种程度上类似于字典——只是语法略有不同。例如，现在你不是写 `s['name']` 或 `s['price']`，而是写 `s.name` 和 `s.price`。
