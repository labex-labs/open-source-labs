# Verbessern der Stock-Klasse

In Python sind Klassen eine leistungsstarke Möglichkeit, Daten und Verhalten zu organisieren. Sie ermöglichen es uns, verwandte Daten und Funktionen zusammenzufassen. In diesem Abschnitt werden wir unsere `Stock`-Klasse verbessern, indem wir eine Methode hinzufügen, die formatierte Aktieninformationen anzeigt. Dies ist ein ausgezeichnetes Beispiel dafür, wie wir sowohl Daten als auch Verhalten in unseren Klassen kapseln können. Kapselung bedeutet, Daten mit den Methoden zusammenzufassen, die auf diesen Daten operieren, was dazu beiträgt, unseren Code organisiert und leichter zu verwalten zu halten.

1. Zunächst müssen Sie die Datei `stock.py` im WebIDE-Editor öffnen. In der `stock.py`-Datei haben wir bisher an unserer `Stock`-Klasse gearbeitet. Indem Sie sie im Editor öffnen, können Sie die Klassendefinition ändern.

2. Jetzt werden wir die `Stock`-Klasse ändern, um eine neue `display()`-Methode hinzuzufügen. Diese Methode wird dafür verantwortlich sein, die Aktieninformationen auf eine schön formatierte Weise auszugeben. So können Sie es machen:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def display(self):
        print(f"Stock: {self.name}, Shares: {self.shares}, Price: ${self.price:.2f}, Total Cost: ${self.cost():.2f}")
```

In der `__init__`-Methode initialisieren wir den Namen der Aktie, die Anzahl der Anteile und den Preis. Die `cost`-Methode berechnet die Gesamtkosten der Aktie, indem sie die Anzahl der Anteile mit dem Preis multipliziert. Die neue `display`-Methode verwendet einen f-String, um die Aktieninformationen, einschließlich des Namens, der Anzahl der Anteile, des Preises und der Gesamtkosten, zu formatieren und auszugeben.

3. Nachdem Sie diese Änderungen vorgenommen haben, müssen Sie die Datei speichern. Sie können dies tun, indem Sie `Strg+S` auf Ihrer Tastatur drücken oder auf das Speicher-Symbol im Editor klicken. Das Speichern der Datei stellt sicher, dass Ihre Änderungen gespeichert werden und später verwendet werden können.

4. Als Nächstes starten wir eine neue Python-Sitzung im interaktiven Modus. Eine interaktive Sitzung ermöglicht es uns, unseren Code sofort zu testen. Um die Sitzung zu starten, führen Sie den folgenden Befehl im Terminal aus:

```bash
python3 -i stock.py
```

Die Option `-i` teilt Python mit, eine interaktive Sitzung nach der Ausführung der `stock.py`-Datei zu starten. Auf diese Weise können wir sofort die `Stock`-Klasse und ihre Methoden verwenden.

5. Jetzt erstellen wir ein Aktienobjekt und verwenden die neue `display()`-Methode. Wir erstellen ein Objekt, das Apple-Aktien repräsentiert, und rufen dann die `display`-Methode auf, um die formatierten Informationen zu sehen. Hier ist der Code:

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

Wenn Sie diesen Code in der interaktiven Sitzung ausführen, sehen Sie die folgende Ausgabe:

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

Diese Ausgabe zeigt, dass die `display`-Methode korrekt funktioniert und die Aktieninformationen wie erwartet formatiert.

6. Schließlich erstellen wir eine Liste von Aktien und zeigen sie alle an. Dies zeigt, wie wir die `display`-Methode mit mehreren Aktienobjekten verwenden können. Hier ist der Code:

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

Wenn Sie diesen Code ausführen, erhalten Sie die folgende Ausgabe:

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

Indem wir die `display()`-Methode zu unserer Klasse hinzugefügt haben, haben wir die Formatierungslogik innerhalb der Klasse selbst gekapselt. Dies macht unseren Code organisierter und leichter zu warten. Wenn wir die Art und Weise ändern müssen, wie die Aktieninformationen angezeigt werden, müssen wir nur die `display`-Methode an einer Stelle ändern, anstatt Änderungen im gesamten Code vorzunehmen.
