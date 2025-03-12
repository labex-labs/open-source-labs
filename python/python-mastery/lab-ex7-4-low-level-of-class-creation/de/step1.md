# Manuelle Klassenerstellung

In der Python-Programmierung sind Klassen ein grundlegendes Konzept, das es Ihnen ermöglicht, Daten und Funktionen zusammenzufassen. Normalerweise definieren wir Klassen mit der Standard-Python-Syntax. Hier ist beispielsweise eine einfache `Stock`-Klasse. Diese Klasse repräsentiert eine Aktie mit Attributen wie `name`, `shares` und `price`, und sie verfügt über Methoden zur Berechnung der Kosten und zum Verkauf von Aktien.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Aber haben Sie sich jemals gefragt, wie Python eine Klasse tatsächlich im Hintergrund erstellt? Was wäre, wenn wir diese Klasse ohne die Standard-Klassen-Syntax erstellen wollten? In diesem Abschnitt werden wir untersuchen, wie Python-Klassen auf einer tieferen Ebene konstruiert werden.

## Starten der interaktiven Python-Shell

Um mit der manuellen Klassenerstellung zu experimentieren, müssen wir eine interaktive Python-Shell öffnen. Diese Shell ermöglicht es uns, Python-Code Zeile für Zeile auszuführen, was ideal für das Lernen und Testen ist.

Öffnen Sie ein Terminal in der WebIDE und starten Sie die interaktive Python-Shell, indem Sie die folgenden Befehle eingeben. Der erste Befehl `cd ~/project` wechselt das aktuelle Verzeichnis in das Projektverzeichnis, und der zweite Befehl `python3` startet die interaktive Python 3-Shell.

```bash
cd ~/project
python3
```

## Definieren von Methoden als normale Funktionen

Bevor wir eine Klasse manuell erstellen, müssen wir die Methoden definieren, die Teil der Klasse sein sollen. In Python sind Methoden einfach Funktionen, die einer Klasse zugeordnet sind. Lassen Sie uns daher die Methoden, die wir in unserer Klasse möchten, als normale Python-Funktionen definieren.

```python
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

def sell(self, nshares):
    self.shares -= nshares
```

Hier ist die `__init__`-Funktion eine spezielle Methode in Python-Klassen. Sie wird Konstruktor genannt und wird verwendet, um die Attribute eines Objekts zu initialisieren, wenn eine Instanz der Klasse erstellt wird. Die `cost`-Methode berechnet die Gesamtkosten der Aktien, und die `sell`-Methode verringert die Anzahl der Aktien.

## Erstellen eines Methoden-Dictionaries

Nachdem wir unsere Methoden als normale Funktionen definiert haben, müssen wir sie so organisieren, dass Python sie beim Erstellen der Klasse verstehen kann. Wir tun dies, indem wir ein Dictionary erstellen, das alle Methoden für unsere Klasse enthält.

```python
methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}
```

In diesem Dictionary sind die Schlüssel die Namen der Methoden, wie sie in der Klasse verwendet werden, und die Werte sind die eigentlichen Funktionsobjekte, die wir zuvor definiert haben.

## Verwenden des `type()`-Konstruktors zur Klassenerstellung

In Python ist die `type()`-Funktion eine eingebaute Funktion, die verwendet werden kann, um Klassen auf einer tieferen Ebene zu erstellen. Die `type()`-Funktion nimmt drei Argumente:

1. Der Name der Klasse: Dies ist eine Zeichenkette, die den Namen der Klasse darstellt, die wir erstellen möchten.
2. Ein Tupel von Basisklassen: In Python können Klassen von anderen Klassen erben. Hier verwenden wir `(object,)`, was bedeutet, dass unsere Klasse von der Basisklasse `object` erbt, die die Basisklasse für alle Klassen in Python ist.
3. Ein Dictionary, das Methoden und Attribute enthält: Dies ist das Dictionary, das wir zuvor erstellt haben und das alle Methoden unserer Klasse enthält.

```python
Stock = type('Stock', (object,), methods)
```

Diese Codezeile erstellt eine neue Klasse namens `Stock` mit der `type()`-Funktion. Die Klasse erbt von der `object`-Klasse und verfügt über die in dem `methods`-Dictionary definierten Methoden.

## Testen unserer manuell erstellten Klasse

Nachdem wir unsere Klasse manuell erstellt haben, lassen Sie uns sie testen, um sicherzustellen, dass sie wie erwartet funktioniert. Wir werden eine Instanz unserer neuen Klasse erstellen und ihre Methoden aufrufen.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
s.sell(25)
print(s.shares)
```

In der ersten Zeile erstellen wir eine Instanz der `Stock`-Klasse mit dem Namen `GOOG`, 100 Aktien und einem Preis von 490,10. Dann geben wir den Namen der Aktie aus, berechnen und geben die Kosten aus, verkaufen 25 Aktien und geben schließlich die verbleibende Anzahl der Aktien aus.

Sie sollten die folgende Ausgabe sehen:

```
GOOG
49010.0
75
```

Diese Ausgabe zeigt, dass unsere manuell erstellte Klasse genau wie eine Klasse funktioniert, die mit der Standard-Python-Syntax erstellt wurde. Sie zeigt, dass eine Klasse im Grunde nur ein Name, ein Tupel von Basisklassen und ein Dictionary von Methoden und Attributen ist. Die `type()`-Funktion konstruiert einfach ein Klassenobjekt aus diesen Komponenten.

Beenden Sie die Python-Shell, wenn Sie fertig sind:

```python
exit()
```
