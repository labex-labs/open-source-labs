# Использование генераторов списков, множеств и словарей

Генераторы в Python - это очень полезный и компактный способ создания новых коллекций на основе существующих. Коллекции в Python могут быть списками, множествами или словарями, которые являются контейнерами для различных типов данных. Генераторы позволяют фильтровать определенные данные, преобразовывать их определенным образом и организовывать более эффективно. В этом разделе мы используем наши данные о портфеле акций, чтобы понять, как работают эти генераторы.

Сначала вам нужно открыть терминал Python, как вы делали на предыдущем этапе. После открытия терминала вы будете поочередно вводить следующие примеры. Такой практический подход поможет вам понять, как работают генераторы на практике.

## Генераторы списков

Генератор списка - это специальный синтаксис в Python, который создает новый список. Он делает это, применяя выражение к каждому элементу существующей коллекции.

Начнем с примера. Сначала мы импортируем функцию для чтения данных о портфеле. Затем мы используем генератор списка, чтобы отфильтровать определенные позиции в портфеле.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

В этом коде мы сначала импортируем функцию `read_portfolio` и используем ее для чтения данных о портфеле из файла CSV. Затем генератор списка `[s for s in portfolio if s['shares'] > 100]` проходит по каждому элементу `s` в коллекции `portfolio`. Он включает элемент `s` в новый список `large_holdings` только в том случае, если количество акций в этой позиции больше 100.

Генераторы списков также можно использовать для выполнения вычислений. Вот несколько примеров:

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

В первом примере генератор списка `[s['shares'] * s['price'] for s in portfolio]` вычисляет общую стоимость каждой позиции в портфеле, умножая количество акций на цену для каждого элемента в `portfolio`. Во втором примере мы используем функцию `sum` вместе с генератором списка, чтобы вычислить общую стоимость всего портфеля.

## Генераторы множеств

Генератор множества используется для создания множества на основе существующей коллекции. Множество - это коллекция, которая содержит только уникальные значения.

Давайте посмотрим, как это работает с нашими данными о портфеле:

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

В этом коде генератор множества `{s['name'] for s in portfolio}` проходит по каждому элементу `s` в `portfolio` и добавляет название акции (`s['name']`) в множество `unique_stocks`. Поскольку множества хранят только уникальные значения, в результате у нас получается список всех различных акций в нашем портфеле без дубликатов.

## Генераторы словарей

Генератор словаря создает новый словарь, применяя выражения для создания пар ключ - значение.

Вот пример использования генератора словаря для подсчета общего количества акций каждой компании в нашем портфеле:

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

В первой строке генератор словаря `{s['name']: 0 for s in portfolio}` создает словарь, в котором каждое название акции (`s['name']`) является ключом, а начальное значение для каждого ключа равно 0. Затем мы используем цикл `for`, чтобы пройти по каждому элементу в `portfolio`. Для каждого элемента мы добавляем количество акций (`s['shares']`) к соответствующему значению в словаре `totals`.

Эти генераторы очень мощные, потому что позволяют преобразовывать и анализировать данные всего несколькими строками кода. Они являются отличным инструментом в вашем арсенале Python - программирования.
