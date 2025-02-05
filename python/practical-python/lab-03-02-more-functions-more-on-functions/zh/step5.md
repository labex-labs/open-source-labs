# 返回值

`return` 语句返回一个值

```python
def square(x):
    return x * x
```

如果没有给出返回值或者缺少 `return` 语句，则返回 `None`。

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# 或者
def foo(x):
    statements  # 没有 `return`

b = foo(4)      # b = None
```
