# Упражнение 3.7: Выбор другого разделителя столбцов

Хотя CSV-файлы довольно распространены, также можно встретить файл, который использует другой разделитель столбцов, такой как табуляция или пробел. Например, файл `portfolio.dat` выглядит так:

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

Функция `csv.reader()` позволяет задать другой разделитель столбцов следующим образом:

```python
rows = csv.reader(f, delimiter=' ')
```

Измените функцию `parse_csv()` в `/home/labex/project/fileparse_3.7.py` так, чтобы она также позволяла изменить разделитель.

Например:

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```
