# Implementierung privater Attribute

In Python verwenden wir eine Namenskonvention, um anzugeben, dass ein Attribut für die interne Verwendung innerhalb einer Klasse vorgesehen ist. Wir versehen diese Attribute mit einem Unterstrich (`_`). Dies signalisiert anderen Entwicklern, dass diese Attribute nicht Teil der öffentlichen API (Application Programming Interface) sind und nicht direkt von außerhalb der Klasse aufgerufen werden sollten.

Betrachten wir die aktuelle `Stock`-Klasse in der Datei `stock.py`. Sie hat eine Klassenvariable namens `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

Die Klassenvariable `types` wird intern verwendet, um Zeilendaten zu konvertieren. Um anzugeben, dass dies ein Implementierungsdetail ist, markieren wir sie als privat.

**Anweisungen:**

1.  Öffnen Sie die Datei `stock.py` im Editor.

2.  Ändern Sie die Klassenvariable `types`, indem Sie einen vorangestellten Unterstrich hinzufügen und sie in `_types` ändern.

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  Aktualisieren Sie die Methode `from_row`, um die umbenannte Variable `_types` zu verwenden.

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  Speichern Sie die Datei `stock.py`.

5.  Erstellen Sie ein Python-Skript namens `test_stock.py`, um Ihre Änderungen zu testen. Sie können die Datei im Editor mit dem folgenden Befehl erstellen:

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  Fügen Sie den folgenden Code zur Datei `test_stock.py` hinzu. Dieser Code erstellt Instanzen der `Stock`-Klasse und gibt Informationen über sie aus.

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

7.  Führen Sie das Testskript mit dem folgenden Befehl im Terminal aus:

    ```bash
    python /home/labex/project/test_stock.py
    ```

    Sie sollten eine ähnliche Ausgabe sehen wie:

    ```
    Name: GOOG, Shares: 100, Price: 490.1
    Cost: 49010.0
    Name: AAPL, Shares: 50, Price: 142.5
    Cost: 7125.0
    ```
