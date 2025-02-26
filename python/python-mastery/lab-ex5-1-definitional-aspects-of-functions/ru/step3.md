# Обдумывание гибкости

В настоящее время две функции в `reader.py` жестко закреплены для работы с именами файлов, которые передаются непосредственно в `open()`. Переработайте код так, чтобы он работал с любым итерируемым объектом, который генерирует строки. Для этого создайте две новые функции `csv_as_dicts(lines, types)` и `csv_as_instances(lines, cls)`, которые преобразуют любую итерируемую последовательность строк. Например:

```python
>>> file = open('portfolio.csv')
>>> port = reader.csv_as_dicts(file, [str, int, float])
>>> port
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
 {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
 {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
 {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```

Основная цель этого заключается в том, чтобы обеспечить возможность работы с разными типами источников ввода. Например:

```python
>>> import gzip
>>> import stock
>>> file = gzip.open('portfolio.csv.gz')
>>> port = reader.csv_as_instances(file, stock.Stock)
>>> port
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
 Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
 Stock('IBM', 100, 70.44)]
>>>
```

Для поддержания обратной совместимости с более старым кодом напишите функции `read_csv_as_dicts()` и `read_csv_as_instances()`, которые принимают имя файла, как раньше. Эти функции должны вызывать `open()` для указанного имени файла и использовать новые функции `csv_as_dicts()` или `csv_as_instances()` для результирующего файла.
