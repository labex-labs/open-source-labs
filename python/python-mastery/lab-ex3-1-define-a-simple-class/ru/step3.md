# Печать таблицы

Поставьте в таблицу данные, прочитанные на шаге 2, и используйте их для создания красиво отформатированной таблицы. Например:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

Возьмите этот код и поместите его в функцию `print_portfolio()`, которая будет выдавать такой же вывод, но дополнительно добавит заголовки таблицы. Например:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

## Примечание:

Завершите функцию `print_portfolio()` в файле `stock.py`.
