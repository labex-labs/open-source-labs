# Возвращение значений

Инструкция `return` возвращает значение

```python
def square(x):
    return x * x
```

Если не задано возвращаемое значение или отсутствует инструкция `return`, возвращается `None`.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# ИЛИ
def foo(x):
    statements  # Отсутствует `return`

b = foo(4)      # b = None
```
