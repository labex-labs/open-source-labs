# Vergleichbarkeit von Objekten mit `__eq__`

In Python ruft Python tatsächlich die spezielle Methode `__eq__` auf, wenn Sie den `==`-Operator verwenden, um zwei Objekte zu vergleichen. Standardmäßig vergleicht diese Methode die Identitäten der Objekte, was bedeutet, dass sie prüft, ob sie an der gleichen Speicheradresse gespeichert sind, anstatt ihren Inhalt zu vergleichen.

Schauen wir uns ein Beispiel an. Nehmen wir an, wir haben eine `Stock`-Klasse und erstellen zwei `Stock`-Objekte mit denselben Werten. Dann versuchen wir, sie mit dem `==`-Operator zu vergleichen. So können Sie es in der Python-Shell tun:

Zuerst starten Sie die Python-Shell, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
python3
```

Dann führen Sie in der Python-Shell den folgenden Code aus:

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

Wie Sie sehen können, hält Python die beiden `Stock`-Objekte `a` und `b` für unterschiedliche Objekte, obwohl sie die gleichen Werte für ihre Attribute (`name`, `shares` und `price`) haben, weil sie an verschiedenen Speicherorten gespeichert sind.

Um dieses Problem zu beheben, können wir die `__eq__`-Methode in unserer `Stock`-Klasse implementieren. Diese Methode wird jedes Mal aufgerufen, wenn der `==`-Operator auf Objekte der `Stock`-Klasse angewendet wird.

Öffnen Sie jetzt erneut die Datei `stock.py`. Fügen Sie innerhalb der `Stock`-Klasse die folgende `__eq__`-Methode hinzu:

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

Lassen Sie uns analysieren, was diese Methode tut:

1. Zuerst verwendet sie die `isinstance`-Funktion, um zu prüfen, ob das `other`-Objekt eine Instanz der `Stock`-Klasse ist. Dies ist wichtig, weil wir nur `Stock`-Objekte mit anderen `Stock`-Objekten vergleichen möchten.
2. Wenn `other` ein `Stock`-Objekt ist, vergleicht sie dann die Attribute (`name`, `shares` und `price`) sowohl des `self`-Objekts als auch des `other`-Objekts.
3. Sie gibt nur `True` zurück, wenn beide Objekte `Stock`-Instanzen sind und ihre Attribute identisch sind.

Nachdem Sie die `__eq__`-Methode hinzugefügt haben, sollte Ihre vollständige `Stock`-Klasse so aussehen:

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

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

Jetzt testen wir unsere verbesserte `Stock`-Klasse. Starten Sie die Python-Shell erneut:

```bash
python3
```

Führen Sie dann den folgenden Code in der Python-Shell aus:

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

Toll! Jetzt können unsere `Stock`-Objekte richtig anhand ihres Inhalts und nicht ihrer Speicheradressen verglichen werden.

Die `isinstance`-Prüfung in der `__eq__`-Methode ist von entscheidender Bedeutung. Sie stellt sicher, dass wir nur `Stock`-Objekte vergleichen. Wenn wir diese Prüfung nicht hätten, könnte das Vergleichen eines `Stock`-Objekts mit etwas, das kein `Stock`-Objekt ist, Fehler verursachen.

Wenn Sie mit dem Testen fertig sind, können Sie die Python-Shell beenden, indem Sie den folgenden Befehl ausführen:

```python
>>> exit()
```
