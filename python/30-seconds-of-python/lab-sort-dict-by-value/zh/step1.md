# 按值排序字典

编写一个名为 `sort_dict_by_value(d, reverse=False)` 的函数，该函数接受一个字典 `d` 并按其值进行排序。该函数应返回一个新字典，其键与原始字典相同，但值按升序排序。如果 `reverse` 参数设置为 `True`，则函数应按降序对字典进行排序。

要解决此问题，你可以按以下步骤操作：

1. 使用 `dict.items()` 从 `d` 中获取一个元组对列表。
2. 使用 lambda 函数和 `sorted()` 对列表进行排序。
3. 使用 `dict()` 将排序后的列表转换回字典。
4. 使用 `sorted()` 中的 `reverse` 参数根据第二个参数按相反顺序对字典进行排序。

**⚠️ 注意：** 字典的值必须是同一类型。

```python
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```
