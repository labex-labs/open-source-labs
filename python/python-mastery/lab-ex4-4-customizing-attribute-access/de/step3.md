# Delegation als Alternative zur Vererbung

Delegation wird manchmal als Alternative zur Vererbung verwendet. Die Idee ist fast die gleiche wie bei der Proxy-Klasse, die Sie in Teil (b) definiert haben. Versuchen Sie, die folgende Klasse zu definieren:

```python
>>> class Spam:
        def a(self):
            print('Spam.a')
        def b(self):
            print('Spam.b')

>>>
```

Nun erstellen Sie eine Klasse, die sich um diese Klasse herumschließt und einige der Methoden neu definiert:

```python
>>> class MySpam:
        def __init__(self):
            self._spam = Spam()
        def a(self):
            print('MySpam.a')
            self._spam.a()
        def c(self):
            print('MySpam.c')
        def __getattr__(self, name):
            return getattr(self._spam, name)

>>> s = MySpam()
>>> s.a()
MySpam.a
Spam.a
>>> s.b()
Spam.b
>>> s.c()
MySpam.c
>>>
```

Beachten Sie genau, dass die resultierende Klasse sehr ähnlich der Vererbung aussieht. Beispielsweise macht die `a()`-Methode etwas ähnliches wie der `super()`-Aufruf. Die `b()`-Methode wird über die `__getattr__()`-Methode abgerufen, die an die intern gehaltene `Spam`-Instanz delegiert.

**Diskussion**

Die `__getattr__()`-Methode wird normalerweise auf Klassen definiert, die als Wrapper um andere Objekte fungieren. Sie müssen jedoch bedenken, dass der Prozess des Umhüllens eines anderen Objekts auf diese Weise oft andere Komplexitäten mit sich bringt. Beispielsweise kann das Wrapperobjekt die Typüberprüfung brechen, wenn ein anderer Teil der Anwendung die `isinstance()`-Funktion verwendet.

Das Delegieren von Methoden über `__getattr__()` funktioniert auch nicht mit speziellen Methoden wie `__getitem__()`, `__enter__()` usw. Wenn eine Klasse solche Methoden intensiv verwendet, müssen Sie ähnliche Funktionen in Ihrer Wrapperklasse bereitstellen.
