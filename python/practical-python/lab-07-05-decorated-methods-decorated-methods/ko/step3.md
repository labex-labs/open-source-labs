# 클래스 메서드 (Class Methods)

`@classmethod`는 클래스 메서드를 정의하는 데 사용됩니다. 클래스 메서드는 인스턴스 대신 _클래스_ 객체를 첫 번째 매개변수로 받습니다.

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

클래스 메서드는 대체 생성자를 정의하는 도구로 가장 자주 사용됩니다.

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

클래스 메서드는 상속과 같은 기능으로 몇 가지 까다로운 문제를 해결합니다.

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
