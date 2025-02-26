# Подготовка

В упражнении 2.6 вы написали модуль `reader.py`, который имел функцию для чтения CSV в список словарей. Например:

```python
>>> import reader
>>> port = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>>
```

Позже мы расширили этот код для работы с экземплярами в упражнении 3.3:

```python
>>> import reader
>>> from stock import Stock
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```

Наконец, код был переработан в набор классов, в котором использовалось наследование, в упражнении 3.7. Однако код стал довольно сложным и запутанным.
