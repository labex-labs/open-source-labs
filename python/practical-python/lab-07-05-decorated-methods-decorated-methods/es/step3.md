# Métodos de clase

`@classmethod` se utiliza para definir métodos de clase. Un método de clase es un método que recibe el objeto de la _clase_ como primer parámetro en lugar de la instancia.

```python
class Foo:
    def bar(self):
        print(self)
    @classmethod
    def spam(cls):
        print(cls)

>>> f = Foo()
>>> f.bar()
<__main__.Foo object at 0x971690>   # La instancia `f`
>>> Foo.spam()
<class '__main__.Foo'>              # La clase `Foo`
>>>
```

Los métodos de clase se utilizan con más frecuencia como una herramienta para definir constructores alternativos.

```python
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        # Observe cómo la clase se pasa como argumento
        tm = time.localtime()
        # Y se utiliza para crear una nueva instancia
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
```

Los métodos de clase resuelven algunos problemas complicados con características como la herencia.

```python
class Date:
 ...
    @classmethod
    def today(cls):
        # Obtiene la clase correcta (por ejemplo, `NewDate`)
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

class NewDate(Date):
 ...

d = NewDate.today()
```
