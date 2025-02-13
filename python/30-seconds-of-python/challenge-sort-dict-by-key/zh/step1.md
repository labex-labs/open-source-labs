# 按键对字典进行排序

## 问题

编写一个函数 `sort_dict_by_key(d, reverse=False)`，该函数接受一个字典 `d`，并返回一个按键排序的新字典。该函数应有一个可选参数 `reverse`，其默认值为 `False`。如果 `reverse` 为 `True`，则字典应按逆序排序。

## 示例

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True) # {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```
