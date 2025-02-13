# 合并字典

## 问题

编写一个函数 `merge_dictionaries(*dicts)`，它接受两个或更多字典作为参数，并返回一个新字典，该字典包含输入字典中的所有键值对。

你的函数应该创建一个新字典，并遍历输入字典，使用 `dictionary.update()` 将每个字典中的键值对添加到结果中。

## 示例

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
