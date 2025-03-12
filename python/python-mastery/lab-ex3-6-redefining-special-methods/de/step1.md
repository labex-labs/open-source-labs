# Verbessern der Objektrepräsentation mit `__repr__`

In Python können Objekte auf zwei verschiedene Arten als Zeichenketten (Strings) dargestellt werden. Diese Darstellungen dienen unterschiedlichen Zwecken und sind in verschiedenen Szenarien nützlich.

Der erste Typ ist die **Zeichenkettenrepräsentation**. Diese wird von der `str()`-Funktion erstellt, die automatisch aufgerufen wird, wenn Sie die `print()`-Funktion verwenden. Die Zeichenkettenrepräsentation ist für die menschliche Lesbarkeit konzipiert. Sie stellt das Objekt in einem Format dar, das für uns leicht zu verstehen und zu interpretieren ist.

Der zweite Typ ist die **Code - Repräsentation**. Diese wird von der `repr()`-Funktion generiert. Die Code - Repräsentation zeigt den Code, den Sie schreiben müssten, um das Objekt neu zu erstellen. Sie geht eher darum, eine präzise und eindeutige Möglichkeit zur Darstellung des Objekts im Code bereitzustellen.

Schauen wir uns ein konkretes Beispiel an, indem wir die eingebaute `date`-Klasse von Python verwenden. Dies wird Ihnen helfen, den Unterschied zwischen der Zeichenketten- und der Code - Repräsentation in der Praxis zu verstehen.

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # Uses str()
2008-07-05
>>> d                     # Uses repr()
datetime.date(2008, 7, 5)
```

In diesem Beispiel ruft Python bei `print(d)` die `str()`-Funktion auf das `date`-Objekt `d` auf, und wir erhalten ein für Menschen lesbares Datum im Format `YYYY-MM-DD`. Wenn wir einfach `d` in der interaktiven Shell eingeben, ruft Python die `repr()`-Funktion auf, und wir sehen den Code, der benötigt wird, um das `date`-Objekt neu zu erstellen.

Sie können die `repr()`-Zeichenkette auf verschiedene Weise explizit abrufen. Hier sind einige Beispiele:

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
```

Jetzt wenden wir dieses Konzept auf unsere `Stock`-Klasse an. Wir werden die Klasse verbessern, indem wir die `__repr__`-Methode implementieren. Diese spezielle Methode wird von Python aufgerufen, wenn es die Code - Repräsentation eines Objekts benötigt.

Um dies zu tun, öffnen Sie die Datei `stock.py` in Ihrem Editor. Fügen Sie dann die `__repr__`-Methode zur `Stock`-Klasse hinzu. Die `__repr__`-Methode sollte eine Zeichenkette zurückgeben, die den Code zeigt, der benötigt wird, um das `Stock`-Objekt neu zu erstellen.

```python
def __repr__(self):
    return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Nachdem Sie die `__repr__`-Methode hinzugefügt haben, sollte Ihre vollständige `Stock`-Klasse jetzt so aussehen:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Jetzt testen wir unsere modifizierte `Stock`-Klasse. Öffnen Sie eine interaktive Python-Shell, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
python3
```

Sobald die interaktive Shell geöffnet ist, versuchen Sie die folgenden Befehle:

```python
>>> import stock
>>> goog = stock.Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
```

Sie können auch sehen, wie die `__repr__`-Methode mit einem Portfolio von Aktien funktioniert. Hier ist ein Beispiel:

```python
>>> import reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
```

Wie Sie sehen können, hat die `__repr__`-Methode unsere `Stock`-Objekte viel informativer gemacht, wenn sie in der interaktiven Shell oder im Debugger angezeigt werden. Sie zeigt jetzt den Code, der benötigt wird, um jedes Objekt neu zu erstellen, was für das Debugging und das Verständnis des Zustands der Objekte sehr nützlich ist.

Wenn Sie mit dem Testen fertig sind, können Sie den Python-Interpreter beenden, indem Sie den folgenden Befehl ausführen:

```python
>>> exit()
```
