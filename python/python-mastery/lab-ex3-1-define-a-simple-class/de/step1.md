# Hinzufügen einer sell-Methode zur Stock-Klasse

In diesem Schritt werden wir die `Stock`-Klasse verbessern, indem wir eine neue Methode hinzufügen. Eine Methode ist wie eine spezielle Funktion, die zu einer Klasse gehört und mit den aus dieser Klasse erstellten Objekten arbeiten kann. Wir werden eine Methode namens `sell(nshares)` erstellen, die uns dabei hilft, den Vorgang des Verkaufs von Aktienanteilen zu simulieren. Wenn Sie Aktienanteile verkaufen, verringert sich die Anzahl der von Ihnen gehaltenen Anteile, und diese Methode wird diese Verringerung für uns handhaben.

## Was ist eine Methode?

Lassen Sie uns zunächst verstehen, was eine Methode ist. Eine Methode ist eine Funktion, die innerhalb einer Klasse definiert wird. Sie ist so konzipiert, dass sie auf Instanzen (die wie individuelle Kopien sind) dieser Klasse operiert. Wenn eine Methode auf einem Objekt aufgerufen wird, kann sie alle Attribute (Eigenschaften) dieses Objekts zugreifen. Sie tut dies über den `self`-Parameter. Der `self`-Parameter ist eine Referenz auf das Objekt, auf dem die Methode aufgerufen wird. Wenn Sie also `self` innerhalb einer Methode verwenden, verweisen Sie auf das spezifische Objekt, auf das die Methode wirkt.

## Implementierungsanweisungen

1. Zunächst müssen wir die Datei `stock.py` im Editor öffnen. Dazu verwenden wir die Befehlszeile. Öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus. Dieser Befehl wechselt das Verzeichnis in den `project`-Ordner, in dem sich die Datei `stock.py` befindet.

```bash
cd ~/project
```

2. Sobald Sie die Datei `stock.py` geöffnet haben, müssen Sie einen bestimmten Kommentar in der `Stock`-Klasse finden. Suchen Sie nach dem Kommentar `# TODO: Add sell(nshares) method here`. Dieser Kommentar ist ein Platzhalter, der angibt, wo wir unsere neue `sell`-Methode hinzufügen sollten.

3. Jetzt ist es an der Zeit, die `sell`-Methode hinzuzufügen. Diese Methode wird einen Parameter namens `nshares` akzeptieren, der die Anzahl der zu verkaufenden Aktienanteile darstellt. Die Hauptaufgabe dieser Methode besteht darin, das `shares`-Attribut des `Stock`-Objekts um die Anzahl der zu verkaufenden Aktienanteile zu verringern.

Hier ist der Code für die `sell`-Methode, den Sie hinzufügen müssen:

```python
def sell(self, nshares):
    self.shares -= nshares
```

In diesem Code bezieht sich `self.shares` auf das `shares`-Attribut des `Stock`-Objekts. Der `-=`-Operator subtrahiert den Wert von `nshares` vom aktuellen Wert von `self.shares`.

4. Nach dem Hinzufügen der `sell`-Methode müssen Sie die Datei `stock.py` speichern. Sie können dies tun, indem Sie `Strg+S` auf Ihrer Tastatur drücken oder "Datei > Speichern" aus dem Menü in Ihrem Editor auswählen.

5. Um sicherzustellen, dass unsere `sell`-Methode korrekt funktioniert, erstellen wir ein Testskript. Erstellen Sie eine neue Python-Datei namens `test_sell.py` und fügen Sie den folgenden Code hinzu:

```python
# test_sell.py
from stock import Stock

# Create a stock object
s = Stock('GOOG', 100, 490.10)
print(f"Initial shares: {s.shares}")

# Sell 25 shares
s.sell(25)
print(f"Shares after selling: {s.shares}")
```

In diesem Skript importieren wir zunächst die `Stock`-Klasse aus der Datei `stock.py`. Dann erstellen wir ein `Stock`-Objekt namens `s` mit dem Aktiensymbol `GOOG`, 100 Anteilen und einem Preis von 490,10. Wir geben die anfängliche Anzahl der Anteile aus. Danach rufen wir die `sell`-Methode auf dem `s`-Objekt auf, um 25 Anteile zu verkaufen. Schließlich geben wir die Anzahl der Anteile nach dem Verkauf aus.

6. Jetzt werden wir das Testskript ausführen, um zu sehen, ob unsere `sell`-Methode wie erwartet funktioniert. Öffnen Sie Ihr Terminal erneut und führen Sie den folgenden Befehl aus:

```bash
python3 test_sell.py
```

Wenn alles korrekt funktioniert, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
Initial shares: 100
Shares after selling: 75
```

Diese Ausgabe bestätigt, dass unsere `sell`-Methode korrekt funktioniert. Sie hat die Anzahl der Anteile erfolgreich um die von uns angegebene Menge verringert.
