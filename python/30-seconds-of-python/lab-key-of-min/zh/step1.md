# 最小值的键

编写一个函数 `key_of_min(d)`，它接受一个字典 `d` 作为参数，并返回该字典中最小值的键。

要解决这个问题，你可以使用内置的 `min()` 函数，并将 `key` 参数设置为 `dict.get()`。这将返回字典中最小值的键。

```python
def key_of_min(d):
  return min(d, key = d.get)
```

```python
key_of_min({'a':4, 'b':0, 'c':13}) # b
```
