# 练习 2.3：一些额外的字典操作

如果你将一个字典转换为列表，你会得到它的所有键：

```python
>>> list(d)
['name','shares', 'price', 'date', 'account']
>>>
```

同样地，如果你使用 `for` 语句在字典上进行迭代，你会得到键：

```python
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

试试这个同时进行查找的变体：

```python
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

你也可以使用 `keys()` 方法获取所有的键：

```python
>>> keys = d.keys()
>>> keys
dict_keys(['name','shares', 'price', 'date', 'account'])
>>>
```

`keys()` 有点不同寻常，因为它返回一个特殊的 `dict_keys` 对象。

这是原始字典的一个覆盖层，它总是会给出当前的键 —— 即使字典发生了变化。例如，试试这个：

```python
>>> del d['account']
>>> keys
dict_keys(['name','shares', 'price', 'date'])
>>>
```

仔细注意，即使你没有再次调用 `d.keys()`，`'account'` 也从 `keys` 中消失了。

一种更优雅的同时处理键和值的方法是使用 `items()` 方法。这会给你 `(键, 值)` 元组：

```python
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

如果你有像 `items` 这样的元组，你可以使用 `dict()` 函数创建一个字典。试试看：

```python
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```
