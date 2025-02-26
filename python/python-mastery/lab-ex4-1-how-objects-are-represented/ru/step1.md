# Подготовка

Начните этот практикум, вернуться к простой версии класса `Stock`, который вы создали. В интерактивном режиме определите новый класс под названием `SimpleStock`, который выглядит так:

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

После определения этого класса создайте несколько экземпляров.

```python
>>> goog = SimpleStock('GOOG',100,490.10)
>>> ibm  = SimpleStock('IBM',50, 91.23)
>>>
```
