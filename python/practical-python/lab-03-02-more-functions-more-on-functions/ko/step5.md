# 값 반환 (Returning Values)

`return` 문은 값을 반환합니다.

```python
def square(x):
    return x * x
```

반환 값이 주어지지 않거나 `return`이 생략된 경우, `None`이 반환됩니다.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# OR
def foo(x):
    statements  # No `return`

b = foo(4)      # b = None
```
