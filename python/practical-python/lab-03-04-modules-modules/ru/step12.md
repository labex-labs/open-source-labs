# Упражнение 3.11: Импорт модулей

В разделе 3 мы создали универсальную функцию `parse_csv()` для разбора содержимого CSV-файлов с данными.

Теперь мы посмотрим, как использовать эту функцию в других программах. Сначала откройте новое окно консоли. Перейдите в папку, где находятся все ваши файлы. Мы собираемся их импортировать.

Запустите интерактивный режим Python.

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

После этого попробуйте импортировать некоторые из ранее написанных вами программ. Вы должны увидеть их вывод точно так же, как и раньше. Чтобы подчеркнуть, импорт модуля запускает его код.

```python
>>> import bounce
... посмотрите на вывод...
>>> import mortgage
... посмотрите на вывод...
>>> import report
... посмотрите на вывод...
>>>
```

Если ничего не работает, вы, вероятно, запускаете Python в неправильной директории. Теперь попробуйте импортировать ваш модуль `fileparse` и получить помощь по нему.

```python
>>> import fileparse
>>> help(fileparse)
... посмотрите на вывод...
>>> dir(fileparse)
... посмотрите на вывод...
>>>
```

Попробуйте использовать модуль для чтения некоторых данных:

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... посмотрите на вывод...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... посмотрите на вывод...
>>> prices = dict(pricelist)
>>> prices
... посмотрите на вывод...
>>> prices['IBM']
106.28
>>>
```

Попробуйте импортировать функцию, чтобы не нужно было указывать имя модуля:

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... посмотрите на вывод...
>>>
```
