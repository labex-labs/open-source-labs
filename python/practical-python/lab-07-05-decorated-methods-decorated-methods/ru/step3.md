# Методы класса

`@classmethod` используется для определения методов класса. Метод класса - это метод, который получает объект _класса_ в качестве первого параметра вместо экземпляра.

```python
class Foo:
    def bar(self):
        print(self)
    @classmethod
    def spam(cls):
        print(cls)

>>> f = Foo()
>>> f.bar()
<__main__.Foo object at 0x971690>   # Экземпляр `f`
>>> Foo.spam()
<class '__main__.Foo'>              # Класс `Foo`
>>>
```

Методы класса чаще всего используются в качестве инструмента для определения альтернативных конструкторов.

```python
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        # Обратите внимание, как класс передается в качестве аргумента
        tm = time.localtime()
        # И используется для создания нового экземпляра
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
```

Методы класса решают некоторые сложные проблемы с такими функциями, как наследование.

```python
class Date:
  ...
    @classmethod
    def today(cls):
        # Получает правильный класс (например, `NewDate`)
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

class NewDate(Date):
  ...

d = NewDate.today()
```
