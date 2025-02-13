# 从字典列表中提取值

## 问题

编写一个函数 `pluck(lst, key)`，它接受一个字典列表 `lst` 和一个键 `key` 作为参数，并返回与指定 `key` 相对应的值列表。

你需要：

- 使用列表推导式和 `dict.get()` 来获取 `lst` 中每个字典的 `key` 值。
- 如果输入列表为空，或者指定的键在任何字典中都不存在，函数应返回一个空列表。

## 示例

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name':'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
print(pluck(simpsons, 'age')) # [8, 36, 34, 10]
```
