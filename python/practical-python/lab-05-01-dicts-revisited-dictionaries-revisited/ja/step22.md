# 演習5.5：継承

`Stock` から継承する新しいクラスを作成します。

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

継承は、属性の検索プロセスを拡張することによって実装されます。`__bases__` 属性は、直近の親クラスのタプルを持っています：

```python
>>> NewStock.__bases__
(<class'stock.Stock'>,)
>>>
```

`__mro__` 属性は、属性の検索対象となるすべての親クラスのタプルを持っています。

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class'stock.Stock'>, <class 'object'>)
>>>
```

上記のインスタンス `n` の `cost()` メソッドが見つけられる方法は次の通りです：

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
