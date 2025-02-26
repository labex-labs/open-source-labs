# Упражнение 5.5: Наследование

Создайте новый класс, который наследуется от `Stock`.

```python
>>> class NewStock(Stock):
        def yow(self):
            print('Yow!')

>>> n = NewStock('ACME', 50, 123.45)
>>> n.cost()
6172.50
>>> n.yow()
Yow!
>>>
```

Наследование реализуется путём расширения процесса поиска атрибутов. Атрибут `__bases__` содержит кортеж непосредственных родителей:

```python
>>> NewStock.__bases__
(<class'stock.Stock'>,)
>>>
```

Атрибут `__mro__` содержит кортеж всех родителей в порядке, в котором они будут искаться при поиске атрибутов.

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class'stock.Stock'>, <class 'object'>)
>>>
```

Вот, как метод `cost()` экземпляра `n` выше будет найден:

```python
>>> for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            break

>>> cls
<class '__main__.Stock'>
>>> cls.__dict__['cost']
<function cost at 0x101aed598>
>>>
```
