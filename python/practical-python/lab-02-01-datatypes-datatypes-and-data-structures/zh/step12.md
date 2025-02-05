# 练习2.2：将字典作为一种数据结构

元组的另一种替代方案是创建一个字典。

```python
>>> d = {
        'name' : row[0],
       'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA','shares': 100, 'price': 32.2 }
>>>
```

计算这种持仓的总成本：

```python
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

将此示例与上面涉及元组的相同计算进行比较。将股票数量改为75。

```python
>>> d['shares'] = 75
>>> d
{'name': 'AA','shares': 75, 'price': 32.2 }
>>>
```

与元组不同，字典可以自由修改。添加一些属性：

```python
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```
