# Задача по анализу данных с использованием данных Чикагской транспортной администрации

Теперь, когда вы потренировались работать с различными структурами данных Python и модулем `collections`, пришло время применить эти навыки в реальной задаче по анализу данных. В этом эксперименте мы будем анализировать данные о пассажиропотоке на автобусах Чикагской транспортной администрации (CTA). Эта практическая работа поможет вам понять, как использовать Python для извлечения значимой информации из реальных наборов данных.

## Понимание данных

Сначала давайте посмотрим на транспортные данные, с которыми мы будем работать. В вашем Python - терминале вы запустите некоторый код, чтобы загрузить данные и понять их базовую структуру.

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

Инструкция `import readrides` импортирует пользовательский модуль, который содержит функцию для чтения данных из файла CSV. Функция `readrides.read_rides_as_dicts` читает данные из указанного файла CSV и преобразует каждую строку в словарь. `len(rows)` дает нам общее количество записей в наборе данных. Выводя первую запись с помощью `pprint.pprint(rows[0])`, мы можем четко увидеть структуру каждой записи.

Данные содержат ежедневные записи о пассажиропотоке на различных автобусных маршрутах. Каждая запись включает:

- `route`: Номер автобусного маршрута
- `date`: Дата в формате "YYYY - MM - DD"
- `daytype`: "W" для буднего дня, "A" для субботы или "U" для воскресенья/праздника
- `rides`: Количество пассажиров в этот день

## Задачи анализа

Давайте по очереди решим каждую из задачи:

### Вопрос 1: Сколько автобусных маршрутов существует в Чикаго?

Чтобы ответить на этот вопрос, нам нужно найти все уникальные номера маршрутов в наборе данных. Мы будем использовать генератор множества для этой задачи.

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

Генератор множества - это компактный способ создания множества. В этом случае мы проходим по каждой строке в списке `rows` и извлекаем значение `route`. Поскольку множество хранит только уникальные элементы, в результате у нас получается множество всех уникальных номеров маршрутов. Вывод длины этого множества дает нам общее количество уникальных автобусных маршрутов.

Мы также можем посмотреть, какие это маршруты:

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

Здесь мы преобразуем множество уникальных маршрутов в список и выводим первые 10 элементов этого списка.

### Вопрос 2: Сколько человек воспользовалось автобусом №22 2 февраля 2011 года?

Для этого вопроса нам нужно отфильтровать данные, чтобы найти конкретную запись, которая соответствует заданному маршруту и дате.

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

Сначала мы определяем переменные `target_date` и `target_route`. Затем мы проходим по каждой строке в списке `rows`. Для каждой строки мы проверяем, совпадают ли `route` и `date` с нашими целевыми значениями. Если совпадение найдено, мы выводим количество пассажиров и выходим из цикла, так как мы нашли запись, которую искали.

Вы можете изменить эти переменные, чтобы проверить любой маршрут в любую дату.

### Вопрос 3: Каково общее количество поездок на каждом автобусном маршруте?

Давайте используем `Counter` для подсчета общего количества поездок на каждом маршруте. `Counter` - это подкласс словаря из модуля `collections`, который используется для подсчета хэшируемых объектов.

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

Сначала мы импортируем класс `Counter` из модуля `collections`. Затем мы инициализируем пустой счетчик с именем `total_rides_by_route`. По мере прохождения по каждой строке в списке `rows` мы добавляем количество поездок на каждом маршруте в счетчик. Наконец, мы используем метод `most_common(5)`, чтобы получить топ - 5 маршрутов с наибольшим общим пассажиропотоком, и выводим результаты.

### Вопрос 4: Какие пять автобусных маршрутов имели наибольший десятилетний рост пассажиропотока с 2001 по 2011 год?

Это более сложная задача. Мы должны сравнить пассажиропоток в 2001 и 2011 годах для каждого маршрута.

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

Сначала мы создаем два объекта `Counter`, `rides_2001` и `rides_2011`, чтобы хранить общий пассажиропоток для каждого маршрута в 2001 и 2011 годах соответственно. По мере прохождения по каждой строке в списке `rows` мы проверяем, начинается ли дата с '2001 -' или '2011 -', и добавляем количество поездок в соответствующий счетчик.

Затем мы создаем пустой словарь `increases`, чтобы хранить рост пассажиропотока для каждого маршрута. Мы проходим по уникальным маршрутам и вычисляем рост, вычитая количество поездок в 2001 году из количества поездок в 2011 году для каждого маршрута.

Чтобы найти топ - 5 маршрутов с наибольшим ростом, мы используем функцию `heapq.nlargest`. Эта функция принимает количество элементов для возврата (в данном случае 5), итерируемый объект (`increases.items()`) и функцию - ключ (`lambda x: x[1]`), которая определяет, как сравнивать элементы.

Наконец, мы выводим результаты, показывая номер маршрута, рост пассажиропотока и количество поездок в 2001 и 2011 годах.

Этот анализ позволяет определить, какие автобусные маршруты испытали наибольший рост пассажиропотока за десятилетие, что может указывать на изменения в демографических показателях, улучшения в обслуживании или другие интересные тенденции.

Вы можете расширить эти анализы различными способами. Например, вы можете:

- Проанализировать модели пассажиропотока по дням недели
- Найти маршруты с снижающимся пассажиропотоком
- Сравнить сезонные колебания в пассажиропотоке

Техники, которые вы узнали в этом эксперименте, предоставляют прочный фундамент для такого рода исследования и анализа данных.
