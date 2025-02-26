# Использование lambda

- lambda имеет серьезные ограничения.
- Разрешается только одно выражение.
- Нет инструкций типа `if`, `while` и т.д.
- Наиболее распространенное использование — с функциями, такими как `sort()`.

Прочитайте некоторые данные портфеля акций и преобразуйте их в список:

```python
>>> import report
>>> portfolio = list(report.read_portfolio('portfolio.csv'))
>>> for s in portfolio:
        print(s)

Stock('AA', 100, 32.2)
Stock('IBM', 50, 91.1)
Stock('CAT', 150, 83.44)
Stock('MSFT', 200, 51.23)
Stock('GE', 95, 40.37)
Stock('MSFT', 50, 65.1)
Stock('IBM', 100, 70.44)
>>>
```
