# Class Methods

`@classmethod` is used to define class methods. A class method is a
method that receives the _class_ object as the first parameter instead
of the instance.

```python
class Foo:
    def bar(self):
        print(self)

    @classmethod
    def spam(cls):
        print(cls)

>>> f = Foo()
>>> f.bar()
<__main__.Foo object at 0x971690>   # The instance `f`
>>> Foo.spam()
<class '__main__.Foo'>              # The class `Foo`
>>>
```

Class methods are most often used as a tool for defining alternate constructors.

```python
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        # Notice how the class is passed as an argument
        tm = time.localtime()
        # And used to create a new instance
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
```

Class methods solve some tricky problems with features like inheritance.

```python
class Date:
    ...
    @classmethod
    def today(cls):
        # Gets the correct class (e.g. `NewDate`)
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

class NewDate(Date):
    ...

d = NewDate.today()
```
