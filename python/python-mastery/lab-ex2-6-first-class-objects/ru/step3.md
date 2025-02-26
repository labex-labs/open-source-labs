# Повторное рассмотрение памяти

В данных о маршрутах автобусов CTA мы установили, что есть 181 уникальных маршрутов автобусов.

```python
>>> routes = { row['route'] for row in rows }
>>> len(routes)
181
>>>
```

Вопрос: Сколько уникальных объектов строковых маршрутов содержится в данных о пассажирах? Вместо создания набора маршрутов создайте набор идентификаторов объектов:

```python
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
542305
>>>
```

Подумайте об этом на минуту - есть только 181 различных имен маршрутов, но результирующий список словарей содержит 542305 разных строковых маршрутов. Возможно, это можно исправить с помощью некоторой кэширования или повторного использования объектов. На самом деле, в Python есть функция, которую можно использовать для кэширования строк, `sys.intern()`. Например:

```python
>>> a = 'hello world'
>>> b = 'hello world'
>>> a is b
False
>>> import sys
>>> a = sys.intern(a)
>>> b = sys.intern(b)
>>> a is b
True
>>>
```

Перезапустите Python и попробуйте это:

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, str, str, int])
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
181
>>>
````

Посмотрите на использование памяти.

```python
>>> tracemalloc.get_traced_memory()
... посмотрите на результат...
>>>
```

Память должна уменьшиться довольно сильно. Замечание: Также есть много повторений, связанных с датами. Что произойдет, если вы также закэшируете строки дат?

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, str, int])
>>> tracemalloc.get_traced_memory()
... посмотрите на результат...
>>>
````
