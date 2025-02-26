# Méthodes de classe

`@classmethod` est utilisé pour définir des méthodes de classe. Une méthode de classe est une méthode qui reçoit l'objet _classe_ en tant que premier paramètre au lieu de l'instance.

```python
class Foo:
    def bar(self):
        print(self)
    @classmethod
    def spam(cls):
        print(cls)

>>> f = Foo()
>>> f.bar()
<__main__.Foo object at 0x971690>   # L'instance `f`
>>> Foo.spam()
<class '__main__.Foo'>              # La classe `Foo`
>>>
```

Les méthodes de classe sont le plus souvent utilisées comme outil pour définir des constructeurs alternatifs.

```python
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        # Remarquez comment la classe est passée en tant qu'argument
        tm = time.localtime()
        # Et utilisée pour créer une nouvelle instance
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
```

Les méthodes de classe résolvent certains problèmes complexes liés aux fonctionnalités telles que l'héritage.

```python
class Date:
  ...
    @classmethod
    def today(cls):
        # Obtient la bonne classe (par exemple `NewDate`)
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

class NewDate(Date):
  ...

d = NewDate.today()
```
