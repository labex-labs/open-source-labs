# 查找具有特定值的键

编写一个名为 `find_keys(dictionary, value)` 的 Python 函数，该函数接受一个字典和一个值作为参数，并返回字典中所有具有给定值的键组成的列表。如果没有键具有给定值，该函数应返回一个空列表。

要解决这个问题，你可以使用 `dictionary.items()` 方法，该方法返回一个生成器，生成字典的键值对。然后，你可以使用列表推导式来过滤出具有给定值的键。

```python
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```
