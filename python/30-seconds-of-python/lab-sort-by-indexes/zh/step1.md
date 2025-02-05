# 根据索引对列表进行排序

编写一个函数 `sort_by_indexes(lst, indexes, reverse=False)`，该函数接受两个列表作为参数，并根据第二个列表的索引返回一个新的已排序列表。该函数应具有以下参数：

- `lst`：要排序的元素列表。
- `indexes`：一个整数列表，表示按其对 `lst` 进行排序的所需索引。
- `reverse`：一个可选的布尔参数，当设置为 `True` 时，按相反顺序对列表进行排序。

该函数应返回一个根据第二个列表的索引排序的新列表。

```python
def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

```python
a = ['eggs', 'bread', 'oranges', 'jam', 'apples','milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam','milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges','milk', 'jam', 'eggs', 'bread', 'apples']
```
