# 准备工作

回到你创建的 `Stock` 类的一个简单版本，以此开始本次实验。在交互式提示符下，定义一个名为 `SimpleStock` 的新类，如下所示：

```python
>>> class SimpleStock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def cost(self):
            return self.shares * self.price

>>>
```

定义好这个类之后，创建几个实例。

```python
>>> goog = SimpleStock('GOOG',100,490.10)
>>> ibm  = SimpleStock('IBM',50, 91.23)
>>>
```
