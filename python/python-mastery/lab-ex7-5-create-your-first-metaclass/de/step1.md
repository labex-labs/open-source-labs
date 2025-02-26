# Erstellen Sie Ihre erste Metaklasse

Erstellen Sie eine Datei namens `mymeta.py` und legen Sie den folgenden Code darin ab (aus den Folien):

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Erstelle Klasse :", name)
        print("Basis-Klassen   :", bases)
        print("Attribute      :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Sobald Sie dies getan haben, definieren Sie eine Klasse, die von `myobject` statt von `object` erbt. Beispielsweise:

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    def sell(self, nshares):
        self.shares -= nshares
```

Versuchen Sie, Ihren Code auszuführen und Instanzen von `Stock` zu erstellen. Sehen Sie, was passiert. Sie sollten die Print-Anweisungen aus Ihrer `mytype` einmal sehen, wenn die `Stock`-Klasse definiert wird.

Was passiert, wenn Sie von `Stock` erben?

```python
class MyStock(Stock):
    pass
```

Sie sollten immer noch Ihre Metaklasse im Einsatz sehen. Metaklassen sind "klebrig", in dem sie über eine gesamte Vererbungshierarchie angewendet werden.

**Diskussion**

Warum möchten Sie so etwas tun? Die Hauptstärke einer Metaklasse besteht darin, dass sie einem Programmierer die Möglichkeit gibt, Details über Klassen kurz vor ihrer Erstellung zu erfassen. Beispielsweise erhalten Sie in der `__new__()`-Methode alle grundlegenden Details, einschließlich des Namens der Klasse, der Basisklassen und der Methodendaten. Wenn Sie diese Daten untersuchen, können Sie verschiedene Arten von diagnostischen Checks durchführen. Wenn Sie wagemutiger sind, können Sie die Daten ändern und verändern, was in der Klassendefinition platziert wird, wenn sie erstellt wird. Keine Angst, es gibt viele Möglichkeiten für schreckliches böses Böses.
