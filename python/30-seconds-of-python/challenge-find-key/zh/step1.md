# 在字典中查找值对应的键

## 问题

编写一个函数 `find_key(dict, val)`，该函数在给定的字典中查找具有给定值的第一个键。

你的函数应该：

- 以字典 `dict` 和值 `val` 作为输入。
- 使用 `dictionary.items()` 和 `next()` 返回第一个值等于 `val` 的键。
- 返回该键作为输出。

## 示例

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
