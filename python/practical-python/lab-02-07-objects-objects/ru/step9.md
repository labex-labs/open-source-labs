# Проверка типа

Как определить, является ли объект определенным типом.

```python
if isinstance(a, list):
    print('a is a list')
```

Проверка на один из нескольких возможных типов.

```python
if isinstance(a, (list,tuple)):
    print('a is a list or tuple')
```

\*Внимание: не злоупотребляйте проверкой типов. Это может привести к чрезмерной сложности кода. Обычно вы будете делать это только в том случае, если это предотвратит распространенные ошибки других, использующих ваш код.
