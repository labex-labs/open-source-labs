# Исследование модуля collections

В Python встроенные контейнеры, такие как списки, словари и множества, очень полезны. Однако модуль `collections` Python позволяет пойти дальше, предоставляя специализированные типы контейнеров, которые расширяют функциональность этих встроенных контейнеров. Давайте более подробно рассмотрим некоторые из этих полезных типов данных.

Вы будете продолжать работать в своем Python - терминале и следовать примерам ниже.

## Counter

Класс `Counter` является подклассом словаря. Его основная цель - подсчитывать хэшируемые объекты. Он предоставляет удобный способ подсчета элементов и поддерживает различные операции.

Сначала нам нужно импортировать класс `Counter` и функцию для чтения портфеля. Затем мы прочитаем портфель из файла CSV.

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

Теперь мы создадим объект `Counter` для подсчета количества акций каждой компании по ее названию.

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

Одной из замечательных особенностей объекта `Counter` является то, что он автоматически инициализирует новые ключи со значением подсчета, равным 0. Это означает, что вам не нужно проверять, существует ли ключ, прежде чем увеличить его счетчик, что упрощает код для накопления подсчетов.

У счетчиков также есть специальные методы. Например, метод `most_common()` очень полезен для анализа данных.

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

Кроме того, счетчики можно комбинировать с помощью арифметических операций.

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## defaultdict

`defaultdict` похож на обычный словарь, но имеет уникальную особенность. Он предоставляет значение по умолчанию для ключей, которые еще не существуют. Это может упростить ваш код, так как вам больше не нужно проверять, существует ли ключ, прежде чем использовать его.

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

Когда вы создаете `defaultdict(list)`, он автоматически создает новый пустой список для каждого нового ключа. Таким образом, вы можете напрямую добавлять элементы в значение ключа, даже если ключ до этого не существовал. Это устраняет необходимость проверять, существует ли ключ, и создавать пустой список вручную.

Вы также можете использовать другие функции - фабрики по умолчанию. Например, вы можете использовать `int`, `float` или даже свою собственную пользовательскую функцию.

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

Эти специализированные типы контейнеров из модуля `collections` могут сделать ваш код более компактным и эффективным при работе с данными.
