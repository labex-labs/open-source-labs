# Einstieg in einfache und multiple Vererbung

In diesem Schritt werden wir uns mit den beiden Hauptarten der Vererbung in Python befassen: einfacher Vererbung und multipler Vererbung. Vererbung ist ein grundlegendes Konzept in der objektorientierten Programmierung, das es einer Klasse ermöglicht, Attribute und Methoden von anderen Klassen zu erben. Wir werden auch untersuchen, wie Python entscheidet, welche Methode aufgerufen wird, wenn es mehrere Kandidaten gibt, ein Prozess, der als Methodenauflösung (Method Resolution) bekannt ist.

## Einfache Vererbung

Einfache Vererbung liegt vor, wenn Klassen eine einzelne Abstammungslinie bilden. Stellen Sie sich das wie ein Stammbaum vor, bei dem jede Klasse nur einen direkten Elternteil hat. Erstellen wir ein Beispiel, um zu verstehen, wie es funktioniert.

Öffnen Sie zunächst ein neues Terminal in der WebIDE. Sobald das Terminal geöffnet ist, starten Sie den Python-Interpreter, indem Sie den folgenden Befehl eingeben und dann die Eingabetaste drücken:

```bash
python3
```

Jetzt, da Sie sich im Python-Interpreter befinden, werden wir drei Klassen erstellen, die eine einfache Vererbungsreihe bilden. Geben Sie den folgenden Code ein:

```python
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()
```

In diesem Code erbt Klasse `B` von Klasse `A`, und Klasse `C` erbt von Klasse `B`. Die `super()`-Funktion wird verwendet, um die Methode der Elternklasse aufzurufen.

Nachdem Sie diese Klassen definiert haben, können wir herausfinden, in welcher Reihenfolge Python nach Methoden sucht. Diese Reihenfolge wird Methodenauflösungsreihenfolge (Method Resolution Order, MRO) genannt. Um die MRO von Klasse `C` anzuzeigen, geben Sie den folgenden Code ein:

```python
C.__mro__
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

Diese Ausgabe zeigt, dass Python zunächst in Klasse `C` nach einer Methode sucht, dann in Klasse `B`, dann in Klasse `A` und schließlich in der Basisklasse `object`.

Jetzt erstellen wir eine Instanz von Klasse `C` und rufen ihre `spam()`-Methode auf. Geben Sie den folgenden Code ein:

```python
c = C()
c.spam()
```

Sie sollten die folgende Ausgabe sehen:

```
C.spam
B.spam
A.spam
```

Diese Ausgabe zeigt, wie `super()` in einer einfachen Vererbungsreihe funktioniert. Wenn `C.spam()` `super().spam()` aufruft, ruft es `B.spam()` auf. Dann, wenn `B.spam()` `super().spam()` aufruft, ruft es `A.spam()` auf.

## Multiple Vererbung

Multiple Vererbung ermöglicht es einer Klasse, von mehr als einer Elternklasse zu erben. Dadurch hat eine Klasse Zugang zu den Attributen und Methoden aller ihrer Elternklassen. Sehen wir uns an, wie die Methodenauflösung in diesem Fall funktioniert.

Geben Sie den folgenden Code in Ihren Python-Interpreter ein:

```python
class Base:
    def spam(self):
        print('Base.spam')

class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()
```

Jetzt erstellen wir eine Klasse `M`, die von mehreren Elternklassen `X`, `Y` und `Z` erbt. Geben Sie den folgenden Code ein:

```python
class M(X, Y, Z):
    pass

M.__mro__
```

Sie sollten die folgende Ausgabe sehen:

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

Diese Ausgabe zeigt die Methodenauflösungsreihenfolge für Klasse `M`. Python wird in dieser Reihenfolge nach Methoden suchen.

Erstellen wir eine Instanz von Klasse `M` und rufen ihre `spam()`-Methode auf:

```python
m = M()
m.spam()
```

Sie sollten die folgende Ausgabe sehen:

```
X.spam
Y.spam
Z.spam
Base.spam
```

Beachten Sie, dass `super()` nicht einfach die Methode der unmittelbaren Elternklasse aufruft. Stattdessen folgt es der von der Kindklasse definierten Methodenauflösungsreihenfolge (MRO).

Erstellen wir eine weitere Klasse `N` mit den Elternklassen in einer anderen Reihenfolge:

```python
class N(Z, Y, X):
    pass

N.__mro__
```

Sie sollten die folgende Ausgabe sehen:

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

Jetzt erstellen wir eine Instanz von Klasse `N` und rufen ihre `spam()`-Methode auf:

```python
n = N()
n.spam()
```

Sie sollten die folgende Ausgabe sehen:

```
Z.spam
Y.spam
X.spam
Base.spam
```

Dies zeigt ein wichtiges Konzept: In Python's multipler Vererbung bestimmt die Reihenfolge der Elternklassen in der Klassendefinition die Methodenauflösungsreihenfolge. Die `super()`-Funktion folgt dieser Reihenfolge, unabhängig von der Klasse, aus der sie aufgerufen wird.

Wenn Sie mit der Erkundung dieser Konzepte fertig sind, können Sie den Python-Interpreter beenden, indem Sie den folgenden Code eingeben:

```python
exit()
```
