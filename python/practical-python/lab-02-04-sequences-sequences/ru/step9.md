# Функция enumerate()

Функция `enumerate` добавляет дополнительное значение счетчика к итерации.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Цикл с i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

Общая форма: `enumerate(sequence [, start = 0])`. `start` является необязательным. Хороший пример использования `enumerate()` - отслеживание номеров строк при чтении файла:

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
     ...
```

В конце концов, `enumerate` - это просто удобный шорткат для:

```python
i = 0
for x in s:
    statements
    i += 1
```

Использование `enumerate` требует меньше набираемых символов и работает немного быстрее.
