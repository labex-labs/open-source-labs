# 映射字典值

## 问题

编写一个函数 `map_values(obj, fn)`，它接受一个字典 `obj` 和一个函数 `fn` 作为参数，并返回一个新字典，其键与原始字典相同，值是通过对每个值运行提供的函数生成的。

## 示例

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```

## 约束条件

- 该函数应适用于任何满足要求的字典和函数。
- 该函数不应修改原始字典。
