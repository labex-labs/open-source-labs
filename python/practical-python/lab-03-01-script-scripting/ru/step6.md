# Определение функции

Функции могут быть _определены_ в любом порядке.

```python
def foo(x):
    bar(x)

def bar(x):
    statements

# ИЛИ
def bar(x):
    statements

def foo(x):
    bar(x)
```

Функции должны быть определены только перед тем, как они будут _использованы_ (или вызваны) во время выполнения программы.

```python
foo(3)        # foo должен быть уже определен
```

С точки зрения стиля, более распространено определять функции в _низу-вверх_ порядке.
