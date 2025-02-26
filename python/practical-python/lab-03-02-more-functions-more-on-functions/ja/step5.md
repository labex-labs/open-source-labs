# 値の返却

`return` 文は値を返します。

```python
def square(x):
    return x * x
```

返却値が指定されていない場合、または `return` が欠けている場合、`None` が返されます。

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# または
def foo(x):
    statements  # return がない

b = foo(4)      # b = None
```
