# Implementierung privater Attribute

In Python, wenn wir eine Klasse entwerfen, gibt es bestimmte Attribute, die nur innerhalb der Klasse selbst verwendet werden sollen. Diese Attribute gehören zur internen Implementierung der Klasse. Um dies anderen Entwicklern zu signalisieren, folgen wir einer Namenskonvention. Wir setzen diesen internen Attributen einen Unterstrich (`_`) voran. Dies ist wie ein Hinweis, dass diese Attribute nicht Teil der öffentlichen API sind. Die öffentliche API ist die Menge an Methoden und Attributen, mit denen andere Teile des Codes interagieren sollen. Daher sollten Attribute mit einem Unterstrich nicht direkt von außerhalb der Klasse zugegriffen werden.

Schauen wir uns die aktuelle `Stock`-Klasse in der Datei `stock.py` an. Diese Klasse wird verwendet, um Aktien zu repräsentieren, und sie hat eine Klassenvariable namens `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

Die Klassenvariable `types` wird innerhalb der Klasse verwendet, um Zeilendaten zu konvertieren. Beispielsweise verwenden wir diese Typen, wenn wir Daten in einer Zeile erhalten, um die Daten in das richtige Format zu konvertieren. Da dies nur ein Implementierungsdetail ist und nicht etwas, mit dem andere Teile des Codes direkt interagieren sollten, sollten wir es als privat markieren.

## Anweisungen:

1. Zuerst müssen wir die Datei `stock.py` im Editor öffnen. Wir können dies mit dem folgenden Befehl im Terminal tun. Dieser Befehl wird die Datei im Code-Editor öffnen.

   ```bash
   code /home/labex/project/stock.py
   ```

2. Jetzt werden wir die Klassenvariable `types` ändern. Wir fügen ihr einen führenden Unterstrich hinzu und machen es zu `_types`. Diese Änderung signalisiert, dass diese Variable privat ist und nicht direkt von außerhalb der Klasse zugegriffen werden sollte.

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Rest of the class...
   ```

3. Nach dem Umbenennen der Variable müssen wir die Methode `from_row` aktualisieren. Diese Methode verwendet die Variable `types`, um Zeilendaten zu konvertieren. Da wir sie jetzt in `_types` umbenannt haben, müssen wir die Methode entsprechend aktualisieren.

   ```python
   @classmethod
   def from_row(cls, row):
       values = [func(val) for func, val in zip(cls._types, row)]
       return cls(*values)
   ```

4. Sobald wir diese Änderungen vorgenommen haben, müssen wir die Datei speichern. Das Speichern der Datei stellt sicher, dass unsere Änderungen gespeichert werden und später verwendet werden können.

5. Um unsere Änderungen zu testen, werden wir ein Python-Skript namens `test_stock.py` erstellen. Wir können die Datei im Editor mit dem folgenden Befehl öffnen.

   ```bash
   code /home/labex/project/test_stock.py
   ```

6. Jetzt fügen wir den folgenden Code zur Datei `test_stock.py` hinzu. Dieser Code erstellt Instanzen der `Stock`-Klasse, sowohl direkt als auch mit der Methode `from_row`. Anschließend gibt er Informationen über diese Instanzen aus, wie den Namen, die Anzahl der Aktien, den Preis und die Kosten.

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
   print(f"Cost: {s.cost()}")

   # Create from row
   row = ['AAPL', '50', '142.5']
   apple = Stock.from_row(row)
   print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
   print(f"Cost: {apple.cost()}")
   ```

7. Schließlich führen wir das Testskript mit dem folgenden Befehl im Terminal aus. Dies wird den Code in der Datei `test_stock.py` ausführen und uns die Ausgabe anzeigen.

   ```bash
   python /home/labex/project/test_stock.py
   ```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Name: AAPL, Shares: 50, Price: 142.5
Cost: 7125.0
```
