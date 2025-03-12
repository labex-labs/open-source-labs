# Erstellen einer einfachen Aktienklasse

In diesem Schritt werden wir eine einfache Klasse erstellen, um eine Aktie darzustellen. Das Verständnis, wie man Klassen erstellt, ist in Python grundlegend, da es uns ermöglicht, reale Objekte und ihr Verhalten zu modellieren. Diese einfache Aktienklasse wird unser Ausgangspunkt sein, um zu untersuchen, wie Python-Objekte intern funktionieren.

Um zu beginnen, müssen wir eine Python interaktive Shell öffnen. Die Python interaktive Shell ist ein ausgezeichneter Ort, um mit Python-Code zu experimentieren. Sie können Python-Befehle nacheinander eingeben und ausführen. Um sie zu öffnen, geben Sie den folgenden Befehl in der Kommandozeile ein:

```bash
python3
```

Sobald Sie den Befehl eingegeben haben, sehen Sie die Python-Eingabeaufforderung (`>>>`). Dies zeigt an, dass Sie jetzt in der Python interaktiven Shell sind und mit dem Schreiben von Python-Code beginnen können.

Jetzt definieren wir eine `SimpleStock`-Klasse. Eine Klasse in Python ist wie ein Bauplan für die Erstellung von Objekten. Sie definiert die Attribute (Daten) und Methoden (Funktionen), die die Objekte dieser Klasse haben werden. So definieren Sie die `SimpleStock`-Klasse mit den erforderlichen Attributen und Methoden:

```python
>>> class SimpleStock:
...     def __init__(self, name, shares, price):
...         self.name = name
...         self.shares = shares
...         self.price = price
...     def cost(self):
...         return self.shares * self.price
...
```

Im obigen Code ist die `__init__`-Methode eine spezielle Methode in Python-Klassen. Sie wird Konstruktor genannt und wird verwendet, um die Attribute eines Objekts zu initialisieren, wenn ein Objekt erstellt wird. Der Parameter `self` bezieht sich auf die Instanz der Klasse, die erstellt wird. Die `cost`-Methode berechnet die Gesamtkosten der Aktien, indem sie die Anzahl der Aktien mit dem Preis pro Aktie multipliziert.

Nachdem wir die Klasse definiert haben, können wir Instanzen der `SimpleStock`-Klasse erstellen. Eine Instanz ist ein tatsächliches Objekt, das aus dem Klassen-Bauplan erstellt wird. Erstellen wir zwei Instanzen, um verschiedene Aktien darzustellen:

```python
>>> goog = SimpleStock('GOOG', 100, 490.10)
>>> ibm = SimpleStock('IBM', 50, 91.23)
```

Diese Instanzen repräsentieren 100 Aktien der Google-Aktie zu einem Preis von 490,10 US-Dollar pro Aktie und 50 Aktien der IBM-Aktie zu einem Preis von 91,23 US-Dollar pro Aktie. Jede Instanz hat ihre eigene Menge an Attributwerten.

Lassen Sie uns überprüfen, ob unsere Instanzen ordnungsgemäß funktionieren. Wir können dies tun, indem wir ihre Attribute überprüfen und ihre Kosten berechnen. Dies wird uns helfen zu bestätigen, dass die Klasse und ihre Methoden wie erwartet funktionieren.

```python
>>> goog.name
'GOOG'
>>> goog.shares
100
>>> goog.price
490.1
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
```

Die `cost()`-Methode multipliziert die Anzahl der Aktien mit dem Preis pro Aktie, um die Gesamtkosten für das Halten dieser Aktien zu berechnen. Durch das Ausführen dieser Befehle können wir sehen, dass die Instanzen die richtigen Attributwerte haben und dass die `cost`-Methode die Kosten korrekt berechnet.
