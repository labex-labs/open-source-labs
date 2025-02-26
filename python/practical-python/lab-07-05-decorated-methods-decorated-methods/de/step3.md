# Klassenmethoden

`@classmethod` wird verwendet, um Klassenmethoden zu definieren. Eine Klassenmethode ist eine Methode, die das _Klass_ -Objekt als erstes Argument statt der Instanz erhält.

```python
class Foo:
    def bar(self):
        print(self)
    @classmethod
    def spam(cls):
        print(cls)

>>> f = Foo()
>>> f.bar()
<__main__.Foo object at 0x971690>   # Die Instanz `f`
>>> Foo.spam()
<class '__main__.Foo'>              # Die Klasse `Foo`
>>>
```

Klassenmethoden werden am häufigsten als Werkzeug zur Definition alternativer Konstruktoren verwendet.

```python
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        # Beachten Sie, wie die Klasse als Argument übergeben wird
        tm = time.localtime()
        # Und verwendet wird, um eine neue Instanz zu erstellen
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
```

Klassenmethoden lösen einige knifflige Probleme mit Funktionen wie Vererbung.

```python
class Date:
 ...
    @classmethod
    def today(cls):
        # Holt die richtige Klasse (z.B. `NewDate`)
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

class NewDate(Date):
 ...

d = NewDate.today()
```
