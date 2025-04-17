# Umwandlung von Methoden in Properties (Eigenschaften)

Properties (Eigenschaften) in Python ermöglichen Ihnen den Zugriff auf berechnete Werte wie Attribute. Dies macht Klammern beim Aufrufen einer Methode überflüssig, wodurch Ihr Code sauberer und konsistenter wird.

Derzeit hat unsere `Stock`-Klasse eine `cost()`-Methode, die die Gesamtkosten der Aktien berechnet.

```python
def cost(self):
    return self.shares * self.price
```

Um den Kostenwert zu erhalten, müssen wir ihn mit Klammern aufrufen:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

Wir können dies verbessern, indem wir die `cost()`-Methode in eine Property (Eigenschaft) umwandeln, wodurch wir auf den Kostenwert ohne Klammern zugreifen können:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**Anweisungen:**

1.  Öffnen Sie die Datei `stock.py` im Editor.

2.  Ersetzen Sie die `cost()`-Methode durch eine Property (Eigenschaft) mithilfe des `@property`-Dekorators:

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  Speichern Sie die Datei `stock.py`.

4.  Erstellen Sie eine neue Datei namens `test_property.py` im Editor:

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  Fügen Sie den folgenden Code zur Datei `test_property.py` hinzu, um eine `Stock`-Instanz zu erstellen und auf die `cost`-Property (Eigenschaft) zuzugreifen:

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

6.  Führen Sie das Testskript aus:

    ```bash
    python /home/labex/project/test_property.py
    ```

    Sie sollten eine ähnliche Ausgabe sehen wie:

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```
