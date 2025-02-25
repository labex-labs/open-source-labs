# Общие习惯用法 для чтения данных из файла

Прочитать весь файл сразу в виде строки.

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` - это строка с всей текстовой информацией из `foo.txt`
```

Прочитать файл построчно с использованием итерации.

```python
with open(filename, 'rt') as file:
    for line in file:
        # Обработать строку
```
