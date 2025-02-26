# Доступ к атрибутам

Существует альтернативный способ доступа, манипуляции и управления атрибутами.

```python
getattr(obj, 'name')          # То же, что и obj.name
setattr(obj, 'name', value)   # То же, что и obj.name = value
delattr(obj, 'name')          # То же, что и del obj.name
hasattr(obj, 'name')          # Проверяет, существует ли атрибут
```

Пример:

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*Примечание: у `getattr()` также есть полезное значение по умолчанию *arg\*.

```python
x = getattr(obj, 'x', None)
```
