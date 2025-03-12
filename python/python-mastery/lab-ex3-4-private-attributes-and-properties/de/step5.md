# Vereinheitlichung der Typvalidierung mit Klassenvariablen

In unserer Python-Programmierreise haben wir eine `Stock`-Klasse erstellt. Diese Klasse verfügt derzeit über zwei verschiedene Methoden zur Handhabung von Datentypen. Das Verständnis dieser Mechanismen ist von entscheidender Bedeutung, da es uns hilft, unseren Code besser zu verwalten und zu organisieren.

Der erste Mechanismus ist die Klassenvariable `_types`. Diese Variable wird verwendet, um Daten aus Zeilen umzuwandeln. Wenn wir Daten in Zeilenformat erhalten, hilft uns die `_types`-Variable, diese Daten in die entsprechenden Typen für unsere `Stock`-Klasse zu transformieren.

Der zweite Mechanismus sind die Property-Setter. Diese Setter erzwingen die Typüberprüfung. Wenn wir versuchen, einen Wert für eine Eigenschaft in unserer `Stock`-Klasse festzulegen, stellen die Property-Setter sicher, dass der Wert vom richtigen Typ ist.

Allerdings kann die Verwendung von zwei getrennten Mechanismen die Wartung unserer Klasse erschweren. Um dieses Problem zu lösen, müssen wir diese beiden Mechanismen vereinheitlichen, sodass sie die gleichen Typinformationen verwenden. Auf diese Weise gewährleisten wir die Konsistenz in unserer Klasse, und sie wird zuverlässiger, wenn wir Unterklassen erstellen.

## Anweisungen:

1. Zuerst müssen wir die Datei `stock.py` im Editor öffnen. Diese Datei enthält den Code für unsere `Stock`-Klasse. Um sie zu öffnen, führen Sie den folgenden Befehl im Terminal aus:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Jetzt werden wir die Property-Setter in der Datei `stock.py` ändern. Wir möchten, dass sie die in der Klassenvariable `_types` definierten Typen verwenden. Dies stellt sicher, dass die Typüberprüfung in den Property-Settern mit der Typumwandlung übereinstimmt, die von der `_types`-Variable durchgeführt wird. So ändern wir die Property-Setter:

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, self._types[1]):
           raise TypeError(f"Expected {self._types[1].__name__}")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, self._types[2]):
           raise TypeError(f"Expected {self._types[2].__name__}")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

3. Nach diesen Änderungen speichern Sie die Datei `stock.py`. Das Speichern der Datei stellt sicher, dass unsere Modifikationen beibehalten werden.

4. Als Nächstes erstellen wir ein Testskript, um zu überprüfen, ob das Erstellen von Unterklassen mit verschiedenen Typen wie erwartet funktioniert. Um dieses Skript zu erstellen, führen Sie den folgenden Befehl im Terminal aus:

   ```bash
   code /home/labex/project/test_subclass.py
   ```

5. Fügen Sie jetzt den folgenden Code zur Datei `test_subclass.py` hinzu. Dieser Code erstellt eine Unterklasse der `Stock`-Klasse mit verschiedenen Typen und testet sowohl die Basisklasse als auch die Unterklasse.

   ```python
   from stock import Stock
   from decimal import Decimal

   # Create a subclass with different types
   class DStock(Stock):
       _types = (str, int, Decimal)

   # Test the base class
   s = Stock('GOOG', 100, 490.10)
   print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

   # Test valid update with float
   try:
       s.price = 500.25
       print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
   except Exception as e:
       print(f"Error updating Stock price: {e}")

   # Test the subclass with Decimal
   ds = DStock('AAPL', 50, Decimal('142.50'))
   print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

   # Test invalid update with float (should require Decimal)
   try:
       ds.price = 150.75
       print(f"Updated DStock price: {ds.price}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")

   # Test valid update with Decimal
   try:
       ds.price = Decimal('155.25')
       print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")
   ```

6. Schließlich führen Sie das Testskript aus, um die Ergebnisse zu sehen. Führen Sie den folgenden Befehl im Terminal aus:

   ```bash
   python /home/labex/project/test_subclass.py
   ```

Wenn Sie das Testskript ausführen, sollten Sie feststellen, dass die Basisklasse `Stock` Fließkommazahlen für den Preis akzeptiert, während die Unterklasse `DStock` `Decimal`-Werte erfordert. Dies zeigt, dass unsere Typvereinheitlichung wie erwartet funktioniert hat.

### Diskussion

Durch die Vereinheitlichung der Typinformationen in unserer `Stock`-Klasse haben wir die Klasse konsistenter gemacht. Jetzt verwenden die Property-Setter die gleichen Typinformationen wie die `from_row`-Methode. Diese Konsistenz erleichtert die Wartung und Erweiterung der Klasse, insbesondere beim Erstellen von Unterklassen.

Obwohl unsere aktuelle Implementierung der `Stock`-Klasse für ein einfaches Konzept komplex erscheinen mag, demonstriert sie wichtige Python-Techniken für Kapselung und Typsicherheit. In realen Anwendungen möchten Sie möglicherweise fortschrittlichere Tools wie Dataclasses oder Drittanbieter-Bibliotheken verwenden, um diese Art von Implementierung zu vereinfachen. Diese Tools können Ihren Code kompakter und leichter zu verwalten machen.
