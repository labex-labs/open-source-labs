# Пример логирования

Рассмотрим функцию.

```python
def add(x, y):
    return x + y
```

Теперь рассмотрим функцию с некоторым логированием добавленным к ней.

```python
def add(x, y):
    print('Calling add')
    return x + y
```

Теперь вторая функция, также с некоторым логированием.

```python
def sub(x, y):
    print('Calling sub')
    return x - y
```
