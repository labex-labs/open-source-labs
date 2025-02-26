# Чтение портфеля

Добавьте функцию `read_portfolio()` в программу `stock.py`, которая читает файл с данными портфеля в список объектов `Stock`. Вот, как это должно работать:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
        print(s)

<__main__.Stock object at 0x3902f0>
<__main__.Stock object at 0x390270>
<__main__.Stock object at 0x390330>
<__main__.Stock object at 0x390370>
<__main__.Stock object at 0x3903b0>
<__main__.Stock object at 0x3903f0>
<__main__.Stock object at 0x390430>
>>>
```

Вы уже писали подобную функцию в рамках упражнения 2.3. Обсуждение дизайна: должна ли `read_portfolio()` быть отдельной функцией или частью определения класса?

## Примечание:

Добавьте функцию `read_portfolio()` в файл `stock.py`.
