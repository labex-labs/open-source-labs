# Печать

Функция `print` выводит одну строку текста со значениями, переданными ей.

```python
print('Hello world!') # Выводит текст 'Hello world!'
```

Можно использовать переменные. Выведенный текст будет значением переменной, а не ее именем.

```python
x = 100
print(x) # Выводит текст '100'
```

Если передать в `print` несколько значений, они будут разделены пробелами.

```python
name = 'Jake'
print('My name is', name) # Выводит текст 'My name is Jake'
```

`print()` всегда добавляет символ новой строки в конце.

```python
print('Hello')
print('My name is', 'Jake')
```

В результате выводится:

```code
Hello
My name is Jake
```

Можно подавить добавление новой строки:

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

Теперь этот код выведет:

```code
Hello My name is Jake
```
