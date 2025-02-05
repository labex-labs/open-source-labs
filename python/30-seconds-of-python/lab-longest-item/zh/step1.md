# 最长的元素

编写一个函数 `longest_item(*args)`，它接受任意数量的可迭代对象或具有长度属性的对象，并返回最长的那个对象。该函数应：

- 使用 `max()` 并以 `len()` 作为 `key` 来返回长度最大的元素。
- 如果多个元素具有相同的长度，则返回第一个元素。

```python
def longest_item(*args):
  return max(args, key = len)
```

```python
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```
