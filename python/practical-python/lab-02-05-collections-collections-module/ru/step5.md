# Упражнение 2.18: Составление таблиц с помощью счетчиков

Предположим, вы хотите составить таблицу общего количества акций каждой компании. Это легко сделать с использованием объектов `Counter`. Попробуйте:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> from collections import Counter
>>> holdings = Counter()
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

Обратите внимание, как несколько записей для `MSFT` и `IBM` в `portfolio` объединяются в одну запись здесь.

Вы можете использовать `Counter` точно так же, как и словарь, чтобы получить отдельные значения:

```python
>>> holdings['IBM']
150
>>> holdings['MSFT']
250
>>>
```

Если вы хотите отсортировать значения, сделайте это так:

```python
>>> # Получить три наиболее популярных акции
>>> holdings.most_common(3)
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
>>>
```

Возьмем другой портфель акций и создадим новый `Counter`:

```python
>>> portfolio2 = read_portfolio('portfolio2.csv')
>>> holdings2 = Counter()
>>> for s in portfolio2:
          holdings2[s['name']] += s['shares']

>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>>
```

Наконец, давайте объединим все портфели с помощью простой операции:

```python
>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>> combined = holdings + holdings2
>>> combined
Counter({'MSFT': 275, 'HPQ': 250, 'GE': 220, 'AA': 150, 'IBM': 150, 'CAT': 150})
>>>
```

Это всего лишь малая часть того, что предоставляют счетчики. Однако, если вы когда-нибудь обнаружите, что нуждаетесь в составлении таблиц значений, стоит рассмотреть использование счетчиков.
