# Смотрите в восторг

Попробуйте запустить свои юнит-тесты из `teststock.py` для этого нового файла. Большинство из них теперь должны проходить. В качестве эксперимента попробуйте использовать свою класс `Stock` с некоторым из раннего кода для форматирования таблиц и чтения данных. Все должно работать.

```python
>>> from stock import Stock
>>> from reader import read_csv_as_instances
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Опять-таки, восхищайтесь конечным файлом `stock.py` и замечайте, насколько чистым выглядит код. Просто постарайтесь не думать о том, что происходит под капотом с базовым классом `Structure`.
