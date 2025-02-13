# 柯里化函数

## 问题

编写一个函数 `curry(fn, *args)`，用于对给定的函数 `fn` 进行柯里化。该函数应返回一个新函数，其行为类似于已部分应用了给定参数 `args` 的 `fn`。

## 示例

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
