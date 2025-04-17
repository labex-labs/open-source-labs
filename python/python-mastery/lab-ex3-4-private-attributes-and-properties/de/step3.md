# Implementierung der Property (Eigenschafts)-Validierung

Properties (Eigenschaften) ermöglichen es Ihnen auch, zu steuern, wie Attributwerte abgerufen, gesetzt und gelöscht werden. Dies ist nützlich, um Ihren Attributen eine Validierung hinzuzufügen und sicherzustellen, dass die Werte bestimmte Kriterien erfüllen.

In unserer `Stock`-Klasse möchten wir sicherstellen, dass `shares` eine nicht-negative Ganzzahl und `price` eine nicht-negative Gleitkommazahl ist. Wir verwenden Property (Eigenschafts)-Dekoratoren zusammen mit Gettern und Settern, um dies zu erreichen.

**Anweisungen:**

1.  Öffnen Sie die Datei `stock.py` im Editor.

2.  Fügen Sie der `Stock`-Klasse private Attribute `_shares` und `_price` hinzu und ändern Sie den Konstruktor, um sie zu verwenden:

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares  # Using private attribute
        self._price = price    # Using private attribute
    ```

3.  Definieren Sie Properties (Eigenschaften) für `shares` und `price` mit Validierung:

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

4.  Aktualisieren Sie den Konstruktor, um die Property (Eigenschafts)-Setter für die Validierung zu verwenden:

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares  # Using property setter
        self.price = price    # Using property setter
    ```

5.  Speichern Sie die Datei `stock.py`.

6.  Erstellen Sie ein Testskript namens `test_validation.py`:

    ```bash
    touch /home/labex/project/test_validation.py
    ```

7.  Fügen Sie den folgenden Code zur Datei `test_validation.py` hinzu:

    ```python
    from stock import Stock

    # Create a valid stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

    # Test valid updates
    try:
        s.shares = 50  # Valid update
        print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting shares=50: {e}")

    try:
        s.price = 123.45  # Valid update
        print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting price=123.45: {e}")

    # Test invalid updates
    try:
        s.shares = "50"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares='50': {e}")

    try:
        s.shares = -10  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares=-10: {e}")

    try:
        s.price = "123.45"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price='123.45': {e}")

    try:
        s.price = -10.0  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price=-10.0: {e}")
    ```

8.  Führen Sie das Testskript aus:

    ```bash
    python /home/labex/project/test_validation.py
    ```

    Sie sollten eine Ausgabe sehen, die erfolgreiche, gültige Aktualisierungen und entsprechende Fehlermeldungen für ungültige Aktualisierungen anzeigt.

    ```plaintext
    Initial: Name=GOOG, Shares=100, Price=490.1, Cost=49010.0
    After setting shares=50: Shares=50, Cost=24505.0
    After setting price=123.45: Price=123.45, Cost=6172.5
    Error setting shares='50': Expected integer
    Error setting shares=-10: shares must be >= 0
    Error setting price='123.45': Expected float
    Error setting price=-10.0: price must be >= 0
    ```
