# 最大值的键

编写一个函数 `key_of_max(d)`，它接受一个字典 `d` 作为参数，并返回字典中最大值的键。如果有多个键具有相同的最大值，则返回其中任何一个。

要解决这个问题，你可以使用 `max()` 函数，并将 `key` 参数设置为 `dict.get()`。这将返回字典中最大值的键。

```python
def key_of_max(d):
  return max(d, key = d.get)
```

```python
key_of_max({'a':4, 'b':0, 'c':13}) # c
```
