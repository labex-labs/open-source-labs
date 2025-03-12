# Implementierung von Eigenschaftsvalidierung

Properties (Eigenschaften) in Python sind ein leistungsstarkes Feature. Sie ermöglichen es Ihnen nicht nur, berechnete Werte so zuzugreifen, als wären es normale Attribute, sondern geben Ihnen auch die Kontrolle darüber, wie diese Attributwerte abgerufen, gesetzt und gelöscht werden. Diese Kontrolle ist äußerst nützlich, wenn Sie Ihre Attribute validieren müssen. Die Validierung stellt sicher, dass die den Attributen zugewiesenen Werte bestimmten Kriterien entsprechen, was dazu beiträgt, die Integrität Ihrer Daten aufrechtzuerhalten.

In unserer `Stock`-Klasse haben wir zwei wichtige Attribute: `shares` und `price`. Wir möchten sicherstellen, dass `shares` eine nicht-negative Ganzzahl und `price` eine nicht-negative Fließkommazahl ist. Um diese Validierung zu erreichen, verwenden wir Property-Dekorateure zusammen mit Gettern und Settern.

## Anweisungen:

1. Zuerst müssen Sie die Datei `stock.py` im Editor öffnen. Hier werden wir alle Änderungen an unserer `Stock`-Klasse vornehmen. Verwenden Sie den folgenden Befehl im Terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. In Python können wir private Attribute verwenden, um die tatsächlichen Werte unserer Klassenvariablen zu speichern. Private Attribute werden durch einen führenden Unterstrich gekennzeichnet. Fügen Sie die privaten Attribute `_shares` und `_price` zur `Stock`-Klasse hinzu und ändern Sie den Konstruktor, um sie zu verwenden. Der Konstruktor ist die Methode, die aufgerufen wird, wenn Sie eine neue Instanz der Klasse erstellen. So geht es:

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self._shares = shares  # Using private attribute
       self._price = price    # Using private attribute
   ```

3. Jetzt definieren wir Properties für `shares` und `price` mit geeigneter Validierung. Properties werden mit dem `@property`-Dekorator für die Getter-Methode und dem `@<property_name>.setter`-Dekorator für die Setter-Methode definiert. Die Getter-Methode wird verwendet, um den Wert des Attributs abzurufen, und die Setter-Methode wird verwendet, um den Wert zu setzen. Hier ist der Code, um Property-Definitionen mit Validierung hinzuzufügen:

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

4. Aktualisieren Sie den Konstruktor, um die Property-Setter zur Validierung zu verwenden. Auf diese Weise werden die Werte von `shares` und `price` automatisch validiert, wenn eine neue Instanz der `Stock`-Klasse erstellt wird. Hier ist der aktualisierte Konstruktor:

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self.shares = shares  # Using property setter
       self.price = price    # Using property setter
   ```

5. Nach all diesen Änderungen speichern Sie die Datei `stock.py`. Dadurch werden Ihre Änderungen gespeichert.

6. Um zu überprüfen, ob unsere Validierung korrekt funktioniert, erstellen wir ein Testskript. Öffnen Sie eine neue Datei namens `test_validation.py` im Editor mit dem folgenden Befehl:

   ```bash
   code /home/labex/project/test_validation.py
   ```

7. Fügen Sie den folgenden Code zur Datei `test_validation.py` hinzu. Dieser Code erstellt eine gültige `Stock`-Instanz und versucht dann, die Attribute `shares` und `price` sowohl mit gültigen als auch mit ungültigen Werten zu aktualisieren. Er gibt auch die Ergebnisse und alle auftretenden Fehlermeldungen aus.

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

8. Schließlich führen Sie das Testskript mit dem folgenden Befehl im Terminal aus:
   ```bash
   python /home/labex/project/test_validation.py
   ```

Sie sollten eine Ausgabe sehen, die erfolgreiche gültige Updates und entsprechende Fehlermeldungen für ungültige Updates anzeigt. Dies bestätigt, dass unsere Eigenschaftsvalidierung wie erwartet funktioniert.
