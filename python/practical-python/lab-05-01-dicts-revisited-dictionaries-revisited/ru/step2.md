# Словарь и модуль

Внутри модуля словарь хранит все глобальные переменные и функции.

```python
# foo.py

x = 42
def bar():
 ...

def spam():
 ...
```

Если вы просмотрите `foo.__dict__` или `globals()`, то увидите словарь.

```python
{
    'x' : 42,
    'bar' : <function bar>,
   'spam' : <function spam>
}
```
