# Имена файлов versus Итерируемые объекты

Сравните эти два программы, которые возвращают один и тот же вывод.

```python
# Предоставьте имя файла
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
         ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# Предоставьте строки
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

- Какую из этих функций вы предпочитаете? Почему?
- Какая из этих функций более гибкая?
