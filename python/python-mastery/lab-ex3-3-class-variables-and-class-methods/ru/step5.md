# Обобщение

Полезной особенностью методов класса является то, что их можно использовать для создания высокоунифицированного интерфейса создания экземпляров для различных классов и написания универсальных служебных функций, которые ими пользуются.

Ранее вы создали файл `reader.py`, в котором были некоторые функции для чтения CSV-данных. Добавьте в файл следующую функцию `read_csv_as_instances()`, которая принимает класс в качестве входных данных и использует метод класса `from_row()` для создания списка экземпляров:

```python
# reader.py
...

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Удалите функцию `read_portfolio()` - вам больше не нужна. Если вы хотите прочитать список объектов `Stock`, сделайте это так:

```python
>>> # Read a portfolio of Stock instances
>>> from reader import read_csv_as_instances
>>> from stock import Stock
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[<__main__.Stock object at 0x100674748>,
<__main__.Stock object at 0x1006746d8>,
<__main__.Stock object at 0x1006747b8>,
<__main__.Stock object at 0x100674828>,
<__main__.Stock object at 0x100674898>,
<__main__.Stock object at 0x100674908>,
<__main__.Stock object at 0x100674978>]
>>>
```

Вот еще один пример использования `read_csv_as_instances()` с совершенно другим классом:

```python
>>> class Row:
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))

>>> rides = read_csv_as_instances('ctabus.csv', Row)
>>> len(rides)
577563
>>>
```

**Обсуждение**

Эта лабораторная работа иллюстрирует два самых распространенных способа использования классовых переменных и методов класса. Классовые переменные часто используются для хранения глобального параметра (например, настройки конфигурации), который общий для всех экземпляров. Иногда подклассы наследуются от базового класса и переопределяют настройку, чтобы изменить поведение.

Методы класса наиболее часто используются для реализации альтернативных конструкторов, как показано выше. Обычный способ определить такие методы класса - это поиск слова "from" в названии. Например, вот пример с встроенными словарями:

```python
>>> d = dict.fromkeys(['a','b','c'], 0)     # class method
>>> d
{'a': 0, 'c': 0, 'b': 0}
>>>
```
