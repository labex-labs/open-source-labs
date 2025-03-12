# Генераторные выражения и эффективность использования памяти

В этом шаге мы рассмотрим генераторные выражения. Они чрезвычайно полезны, когда вы работаете с большими наборами данных в Python. Они могут сделать ваш код гораздо более экономным по памяти, что является важным фактором при работе с большим объемом данных.

## Понимание генераторных выражений

Генераторное выражение похоже на списочное включение, но есть важное различие. Когда вы используете списочное включение, Python сразу создает список со всеми результатами. Это может занять много памяти, особенно если вы работаете с большим набором данных. С другой стороны, генераторное выражение порождает результаты по одному по мере необходимости. Это означает, что оно не нужно хранить все результаты в памяти сразу, что может сэкономить значительное количество памяти.

Давайте рассмотрим простой пример, чтобы понять, как это работает:

```python
# Start a new Python session if needed
# python3

# List comprehension (creates a list in memory)
nums = [1, 2, 3, 4, 5]
squares_list = [x*x for x in nums]
print(squares_list)

# Generator expression (creates a generator object)
squares_gen = (x*x for x in nums)
print(squares_gen)  # This doesn't print the values, just the generator object

# Iterate through the generator to get values
for n in squares_gen:
    print(n)
```

При запуске этого кода вы увидите следующий вывод:

```
[1, 4, 9, 16, 25]
<generator object <genexpr> at 0x7f...>
1
4
9
16
25
```

Важно отметить, что генераторы можно пройти только один раз. После того, как вы переберете все значения в генераторе, он исчерпается, и вы не сможете получить эти значения снова.

```python
# Try to iterate again over the same generator
for n in squares_gen:
    print(n)  # Nothing will be printed, as the generator is already exhausted
```

Вы также можете вручную получать значения из генератора по одному с использованием функции `next()`.

```python
# Create a fresh generator
squares_gen = (x*x for x in nums)

# Get values one by one
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
```

Когда в генераторе больше нет значений, вызов `next()` вызовет исключение `StopIteration`.

## Генераторные функции с использованием `yield`

Для более сложной логики генераторов вы можете написать генераторные функции с использованием оператора `yield`. Генераторная функция - это особый тип функции, которая использует `yield` для возврата значений по одному, а не возврата одного результата сразу.

```python
def squares(nums):
    for x in nums:
        yield x*x

# Use the generator function
for n in squares(nums):
    print(n)
```

При запуске этого кода вы увидите следующий вывод:

```
1
4
9
16
25
```

## Снижение потребления памяти с помощью генераторных выражений

Теперь давайте посмотрим, как генераторные выражения могут сэкономить память при работе с большими наборами данных. Мы будем использовать файл данных о автобусах CTA, который довольно большой.

Сначала попробуем подход, который требует много памяти:

```python
import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Теперь выйдите из Python и перезапустите его, чтобы сравнить с подходом на основе генераторов:

```bash
exit() python3
```

```python
import tracemalloc
tracemalloc.start()

import csv
f = open('ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

# Use generator expressions for all operations
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Вы должны заметить значительную разницу в потреблении памяти между этими двумя подходами. Подход на основе генераторов обрабатывает данные по частям, не загружая все сразу в память, что намного более экономично по памяти.

## Генераторные выражения с функциями-редукторами

Генераторные выражения особенно полезны в сочетании с функциями, такими как `sum()`, `min()`, `max()`, `any()` и `all()`, которые обрабатывают целую последовательность и возвращают один результат.

Давайте рассмотрим несколько примеров:

```python
from readport import read_portfolio
portfolio = read_portfolio('portfolio.csv')

# Calculate the total value of the portfolio
total_value = sum(s['shares']*s['price'] for s in portfolio)
print(f"Total portfolio value: {total_value}")

# Find the minimum number of shares in any holding
min_shares = min(s['shares'] for s in portfolio)
print(f"Minimum shares in any holding: {min_shares}")

# Check if any stock is IBM
has_ibm = any(s['name'] == 'IBM' for s in portfolio)
print(f"Portfolio contains IBM: {has_ibm}")

# Check if all stocks are IBM
all_ibm = all(s['name'] == 'IBM' for s in portfolio)
print(f"All stocks are IBM: {all_ibm}")

# Count IBM shares
ibm_shares = sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
print(f"Total IBM shares: {ibm_shares}")
```

Генераторные выражения также полезны для операций со строками. Вот как можно объединить значения в кортеже:

```python
s = ('GOOG', 100, 490.10)
# This would fail: ','.join(s)
# Use a generator expression to convert all items to strings
joined = ','.join(str(x) for x in s)
print(joined)  # Output: 'GOOG,100,490.1'
```

Основное преимущество использования генераторных выражений в этих примерах заключается в том, что не создаются промежуточные списки, что приводит к более экономичному по памяти коду.
