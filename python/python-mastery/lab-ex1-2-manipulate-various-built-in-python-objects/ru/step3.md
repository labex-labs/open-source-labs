# Работа со списками в Python

Списки - это тип структуры данных в Python. Структура данных представляет собой способ организации и хранения данных для их эффективного использования. Списки очень универсальны, так как могут хранить различные типы элементов, такие как числа, строки или даже другие списки. В этом разделе мы научимся выполнять различные операции над списками.

## Создание списков из строк

Для начала работы со списками в Python нам нужно открыть интерактивную сессию Python. Это своего рода специальная среда, в которой мы можем сразу же писать и запускать код Python. Чтобы начать эту сессию, введите следующую команду в терминале:

```bash
python3
```

После того, как вы находитесь в интерактивной сессии Python, мы создадим список из строки. Строка представляет собой последовательность символов. Мы определим строку, содержащую некоторые тикеры акций, разделенные пробелами. Затем мы преобразуем эту строку в список. Каждый тикер акции станет элементом списка.

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # Разделить строку по пробелам
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

Метод `split()` используется для разделения строки на части в местах, где есть пробел. Каждая часть становится элементом нового списка.

## Доступ и изменение элементов списка

Как и строки, списки поддерживают индексацию. Индексация означает, что мы можем получить доступ к отдельным элементам списка по их позиции. В Python первый элемент списка имеет индекс 0, второй - индекс 1 и так далее. Мы также можем использовать отрицательную индексацию для доступа к элементам с конца списка. Последний элемент имеет индекс -1, предпоследний - индекс -2 и так далее.

В отличие от строк, элементы списка можно изменять. Это означает, что мы можем изменить значение элемента в списке.

```python
>>> symlist[0]    # Первый элемент
'HPQ'
>>> symlist[1]    # Второй элемент
'AAPL'
>>> symlist[-1]   # Последний элемент
'GOOG'
>>> symlist[-2]   # Предпоследний элемент
'YHOO'

>>> symlist[2] = 'AIG'    # Заменить третий элемент
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
```

## Итерация по списку

Часто нам нужно выполнить одну и ту же операцию над каждым элементом списка. Для этого мы можем использовать цикл `for`. Цикл `for` позволяет пройти по каждому элементу списка по очереди и выполнить над ним определенное действие.

```python
>>> for s in symlist:
...     print('s =', s)
...
```

При запуске этого кода вы увидите, что каждый элемент списка выводится с меткой `s =`.

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## Проверка наличия элемента

Иногда нам нужно проверить, существует ли определенный элемент в списке. Для этого мы можем использовать оператор `in`. Оператор `in` возвращает `True`, если элемент находится в списке, и `False`, если его нет.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## Добавление и удаление элементов

Списки имеют встроенные методы, которые позволяют добавлять и удалять элементы. Метод `append()` добавляет элемент в конец списка. Метод `insert()` вставляет элемент в определенную позицию списка. Метод `remove()` удаляет элемент из списка по его значению.

```python
>>> symlist.append('RHT')    # Добавить элемент в конец
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.insert(1, 'AA')    # Вставить в определенную позицию
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.remove('MSFT')    # Удалить по значению
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Если вы попытаетесь удалить элемент, который не существует в списке, Python выдаст ошибку.

```python
>>> symlist.remove('MSFT')
```

Вы увидите сообщение об ошибке следующего вида:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

Мы также можем найти позицию элемента в списке с помощью метода `index()`.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # Проверить элемент в этой позиции
'YHOO'
```

## Сортировка списков

Списки можно отсортировать на месте, то есть исходный список будет изменен. Мы можем отсортировать список в алфавитном порядке или в обратном порядке.

```python
>>> symlist.sort()    # Отсортировать в алфавитном порядке
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # Отсортировать в обратном порядке
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## Вложенные списки

Списки могут содержать любые типы объектов, в том числе и другие списки. Это называется вложенным списком.

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Для доступа к элементам вложенного списка мы используем несколько индексов. Первый индекс выбирает элемент внешнего списка, а второй индекс выбирает элемент внутреннего списка.

```python
>>> items[0]    # Первый элемент (symlist)
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]    # Второй элемент в symlist
'RHT'
>>> items[0][1][2]    # Третий символ в 'RHT'
'T'
>>> items[1]    # Второй элемент (список nums)
[101, 102, 103]
>>> items[1][1]    # Второй элемент в nums
102
```

Когда вы закончите работу в интерактивной сессии Python, вы можете выйти из нее, введя:

```python
>>> exit()
```
