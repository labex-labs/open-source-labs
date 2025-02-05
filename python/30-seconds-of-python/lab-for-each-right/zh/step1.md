# 反向为每个列表元素执行函数

编写一个函数 `for_each_right(itr, fn)`，它接受一个列表 `itr` 和一个函数 `fn` 作为参数。该函数应从最后一个元素开始，为 `itr` 中的每个元素执行一次 `fn`。

```python
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)
```

```python
for_each_right([1, 2, 3], print) # 3 2 1
```
