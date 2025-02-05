# 常见操作

要从字典中获取值，请使用键名。

```python
>>> print(s['name'], s['shares'])
GOOG 100
>>> s['price']
490.10
>>>
```

要添加或修改值，请使用键名进行赋值。

```python
>>> s['shares'] = 75
>>> s['date'] = '6/6/2007'
>>>
```

要删除一个值，请使用 `del` 语句。

```python
>>> del s['date']
>>>
```
