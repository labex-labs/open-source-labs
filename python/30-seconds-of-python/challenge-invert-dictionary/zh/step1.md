# 反转字典

## 问题

编写一个名为 `invert_dictionary(obj)` 的Python函数，该函数接受一个字典 `obj` 作为参数，并返回一个键值颠倒的新字典。输入字典 `obj` 将具有唯一的可哈希值。输出字典应具有与输入字典相同的键，但值应为输入字典中的键。

你应该使用 `dictionary.items()` 并结合列表推导式来创建新字典。

## 示例

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```
