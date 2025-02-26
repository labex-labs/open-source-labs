# Упражнение 3.9: Захват исключений

Функция `parse_csv()`, которую вы написали, используется для обработки всего содержимого файла. Однако, в реальности возможны поврежденные, отсутствующие или "грязные" данные в входных файлах. Попробуйте этот эксперимент:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Измените функцию `parse_csv()` так, чтобы она ловила все исключения `ValueError`, возникающие при создании записей, и выводила сообщение об ошибке для строк, которые не могут быть преобразованы.

Сообщение должно включать номер строки и информацию о причине неудачи. Чтобы протестировать функцию, попробуйте прочитать файл `missing.csv` выше. Например:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Строка 4: Не удалось преобразовать ['MSFT', '', '51.23']
Строка 4: Причина: invalid literal for int() with base 10: ''
Строка 7: Не удалось преобразовать ['IBM', '', '70.44']
Строка 7: Причина: invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```
