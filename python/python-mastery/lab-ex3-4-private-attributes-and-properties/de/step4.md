# Verwendung von `__slots__` zur Speicheroptimierung

Das Attribut `__slots__` beschränkt die Attribute, die eine Klasse haben kann. Es verhindert das Hinzufügen neuer Attribute zu Instanzen und reduziert die Speichernutzung.

In unserer `Stock`-Klasse verwenden wir `__slots__`, um:

1.  Die Attributerstellung auf die von uns definierten Attribute zu beschränken.
2.  Die Speichereffizienz zu verbessern, insbesondere beim Erstellen vieler Instanzen.

**Anweisungen:**

1.  Öffnen Sie die Datei `stock.py` im Editor.
2.  Fügen Sie eine `__slots__`-Klassenvariable hinzu, die alle von der Klasse verwendeten privaten Attributnamen auflistet:

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  Speichern Sie die Datei.

4.  Erstellen Sie ein Testskript namens `test_slots.py`:

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  Fügen Sie den folgenden Code zur Datei `test_slots.py` hinzu:

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  Führen Sie das Testskript aus:

    ```bash
    python /home/labex/project/test_slots.py
    ```

    Sie sollten eine Ausgabe sehen, die zeigt, dass Sie auf die definierten Attribute zugreifen können, aber der Versuch, ein neues Attribut hinzuzufügen, einen `AttributeError` auslöst.

    ```plaintext
    Name: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    Error: 'Stock' object has no attribute 'extra'
    ```
