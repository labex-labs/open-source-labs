# 字典的值

你会得到一个扁平字典，你需要创建一个函数，该函数返回字典中所有值的扁平列表。你的任务是实现 `values_only(flat_dict)` 函数，该函数以扁平字典作为参数，并返回字典中所有值的列表。

要解决这个问题，你可以使用 `dict.values()` 方法来返回给定字典中的值。然后，你可以使用 `list()` 函数将结果转换为列表。

```python
def values_only(flat_dict):
  return list(flat_dict.values())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```
