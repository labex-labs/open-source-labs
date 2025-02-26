# Statische Methoden

`@staticmethod` wird verwendet, um sogenannte _statische_ Klassenmethoden (aus C++/Java) zu definieren. Eine statische Methode ist eine Funktion, die Teil der Klasse ist, aber auf Instanzen _nicht_ operiert.

```python
class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)

>>> Foo.bar(2) # x=2
>>>
```

Statische Methoden werden manchmal verwendet, um internen Unterstützungs-Code für eine Klasse zu implementieren. Beispielsweise Code, um die erstellten Instanzen zu verwalten (Speicherverwaltung, Systemressourcen, Persistenz, Sperren usw.). Sie werden auch von bestimmten Designmustern verwendet (hier nicht behandelt).
