# Построение списка

Создание списка с нуля.

```python
records = []  # Инициализация пустого списка

# Используйте.append(), чтобы добавить больше элементов
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

Пример чтения записей из файла.

```python
records = []  # Инициализация пустого списка

with open('portfolio.csv', 'rt') as f:
    next(f) # Пропустить заголовок
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```
