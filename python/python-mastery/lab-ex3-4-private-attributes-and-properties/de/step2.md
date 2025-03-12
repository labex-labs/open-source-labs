# Konvertieren von Methoden in Properties

In Python sind Properties (Eigenschaften) ein leistungsstarkes Feature, das es Ihnen ermöglicht, berechnete Werte auf eine Weise zuzugreifen, die der Zugriffsmethode auf Attribute ähnelt. Normalerweise müssen Sie, wenn Sie einen Wert aus einer Methode abrufen möchten, Klammern verwenden, um diese Methode aufzurufen. Mit Properties entfällt jedoch die Notwendigkeit dieser Klammern, wodurch Ihr Code sauberer aussieht und konsistenter mit der Art und Weise ist, wie Sie auf normale Attribute zugreifen.

Schauen wir uns unsere aktuelle `Stock`-Klasse an. Sie hat eine Methode `cost()`, die die Gesamtkosten der Aktien berechnet. Diese Methode multipliziert die Anzahl der Aktien mit dem Preis pro Aktie, um uns die Gesamtkosten zu geben. So sieht die `cost()`-Methode aus:

```python
def cost(self):
    return self.shares * self.price
```

Um den Kostenwert mit dieser Methode abzurufen, müssen wir sie mit Klammern aufrufen, wie hier:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

Aber wir können unseren Code verbessern. Indem wir die `cost()`-Methode in eine Property umwandeln, können wir auf den Kostenwert zugreifen, genau wie auf andere Attribute, ohne Klammern zu verwenden. So würde es aussehen:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

## Anweisungen:

1. Zuerst müssen wir die Datei `stock.py` im Editor öffnen. Hier ist die `Stock`-Klasse definiert, und wir werden Änderungen daran vornehmen. Verwenden Sie den folgenden Befehl im Terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Innerhalb der Datei `stock.py` werden wir die `cost()`-Methode durch eine Property ersetzen. Wir verwenden dazu den `@property`-Dekorator. Der `@property`-Dekorator teilt Python mit, dass die folgende Methode als Property behandelt werden soll. Ersetzen Sie die `cost()`-Methode durch den folgenden Code:

   ```python
   @property
   def cost(self):
       return self.shares * self.price
   ```

3. Nach den Änderungen speichern Sie die Datei `stock.py`. Dadurch werden unsere Modifikationen gespeichert und können später verwendet werden.

4. Jetzt müssen wir ein einfaches Python-Skript erstellen, um unsere neue Property zu testen. Öffnen Sie eine neue Datei namens `test_property.py` im Editor mit dem folgenden Befehl:

   ```bash
   code /home/labex/project/test_property.py
   ```

5. In der Datei `test_property.py` fügen wir einige Codezeilen hinzu, um eine `Stock`-Instanz zu erstellen und auf die `cost`-Property zuzugreifen. Hier ist der Code, den Sie hinzufügen sollten:

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)

   # Access cost as a property (no parentheses)
   print(f"Stock: {s.name}")
   print(f"Shares: {s.shares}")
   print(f"Price: {s.price}")
   print(f"Cost: {s.cost}")  # Using the property
   ```

6. Schließlich führen Sie das Testskript aus, um zu sehen, ob unsere Property wie erwartet funktioniert. Verwenden Sie den folgenden Befehl im Terminal:
   ```bash
   python /home/labex/project/test_property.py
   ```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0
```

Beachten Sie, wie wir jetzt auf `cost` als auf ein Attribut zugreifen können (ohne Klammern), wodurch unser Code konsistenter mit der Art und Weise wird, wie wir auf andere Attribute wie `name`, `shares` und `price` zugreifen. Dies macht unseren Code leichter lesbar und wartbar.
