# 字典转列表

编写一个函数 `dict_to_list(d)`，它接受一个字典 `d` 作为参数，并返回一个元组列表。每个元组应包含字典中的一个键值对。列表中元组的顺序应与字典中键值对的顺序相同。

```python
def dict_to_list(d):
  return list(d.items())
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
```
