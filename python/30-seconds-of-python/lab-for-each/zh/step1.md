# 对列表的每个元素执行函数

编写一个函数 `for_each(itr, fn)`，它接受一个列表 `itr` 和一个函数 `fn` 作为参数。该函数应该对 `itr` 中的每个元素执行一次 `fn`。

```python
def for_each(itr, fn):
  for el in itr:
    fn(el)
```

```python
for_each([1, 2, 3], print) # 1 2 3
```
