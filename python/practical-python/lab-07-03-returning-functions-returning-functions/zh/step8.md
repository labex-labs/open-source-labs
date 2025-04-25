# 练习 7.8：简化函数调用

在上述示例中，用户可能会觉得像`typedproperty('shares', int)`这样的调用输入起来有点冗长 —— 尤其是如果它们被大量重复使用时。在`typedproperty.py`文件中添加以下定义：

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

现在，重写`Stock`类以使用这些函数：

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

啊，这样好多了。这里的主要收获是闭包和`lambda`通常可以用来简化代码并消除烦人的重复。这通常是件好事。
