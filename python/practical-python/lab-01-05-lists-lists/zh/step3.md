# 列表迭代与搜索

使用 `for` 循环来遍历列表中的内容。

```python
for name in names:
    # 使用 name
    # 例如 print(name)
  ...
```

这类似于其他编程语言中的 `foreach` 语句。

要快速找到某个元素的位置，使用 `index()` 方法。

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

如果元素出现不止一次，`index()` 将返回第一次出现的索引。

如果未找到该元素，它将引发 `ValueError` 异常。
