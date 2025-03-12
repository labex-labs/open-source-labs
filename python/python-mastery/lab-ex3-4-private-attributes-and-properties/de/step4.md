# Verwendung von `__slots__` zur Speicheroptimierung

In Python ist das `__slots__`-Attribut ein spezielles Werkzeug, das Ihnen hilft, Ihre Klassen effizienter zu verwalten. Es schränkt die Attribute ein, die eine Klasse haben kann. Normalerweise speichert Python Instanzattribute in einem Wörterbuch namens `__dict__`, das die dynamische Hinzufügung neuer Attribute ermöglicht. Wenn Sie jedoch `__slots__` definieren, erstellt Python eine statische Struktur für die Instanzen. Dies hat zwei Hauptauswirkungen: Es verhindert das Hinzufügen neuer Attribute zu den Instanzen, und es reduziert den Speicherverbrauch, da es nicht das `__dict__` pflegen muss.

In unserer `Stock`-Klasse verwenden wir `__slots__` aus zwei wichtigen Gründen:

1. Um die Attributerstellung auf nur die Attribute zu beschränken, die wir definiert haben. Dies bedeutet, dass Benutzer der Klasse nicht versehentlich oder absichtlich neue Attribute hinzufügen können, die wir nicht geplant haben.
2. Um die Speichereffizienz zu verbessern, insbesondere wenn viele Instanzen erstellt werden. Wenn Sie eine große Anzahl von Objekten der `Stock`-Klasse haben, kann die Verwendung von `__slots__` eine beträchtliche Menge an Speicher sparen.

## Anweisungen:

1. Zuerst müssen Sie die Datei `stock.py` im Editor öffnen. Hier werden wir Änderungen an der `Stock`-Klasse vornehmen. Verwenden Sie den folgenden Befehl im Terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Innerhalb der Datei `stock.py` fügen wir eine Klassenvariable `__slots__` hinzu. Diese Variable sollte alle privaten Attributnamen auflisten, die von der Klasse verwendet werden. So geht es:

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Define slots to restrict attribute creation
       __slots__ = ('name', '_shares', '_price')

       # Rest of the class...
   ```

   Indem wir `__slots__` so definieren, sagen wir Python, dass Instanzen der `Stock`-Klasse nur die Attribute `name`, `_shares` und `_price` haben können.

3. Nach diesen Änderungen speichern Sie die Datei. Dies stellt sicher, dass Ihre Modifikationen gespeichert werden.

4. Jetzt müssen wir ein Testskript erstellen, um zu überprüfen, ob `__slots__` wie erwartet funktioniert. Öffnen Sie eine neue Datei namens `test_slots.py` mit dem folgenden Befehl:

   ```bash
   code /home/labex/project/test_slots.py
   ```

5. Fügen Sie den folgenden Code zur Datei `test_slots.py` hinzu. Dieser Code erstellt eine Instanz der `Stock`-Klasse, greift auf ihre vorhandenen Attribute zu und versucht dann, ein neues Attribut hinzuzufügen.

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

   Der `try`-Block versucht, ein neues Attribut `extra` zur `Stock`-Instanz `s` hinzuzufügen. Wenn `__slots__` korrekt funktioniert, sollte dies einen `AttributeError` auslösen, da `extra` nicht in `__slots__` aufgeführt ist.

6. Schließlich führen Sie das Testskript mit dem folgenden Befehl aus:
   ```bash
   python /home/labex/project/test_slots.py
   ```

Sie sollten eine Ausgabe sehen, die zeigt, dass Sie auf die definierten Attribute zugreifen können, aber das Versuch, ein neues Attribut hinzuzufügen, einen `AttributeError` auslöst. Dies bestätigt, dass `__slots__` wie beabsichtigt funktioniert.

### Verständnis von `__slots__`

Beim Verwenden von `__slots__` ist es wichtig, die folgenden Punkte im Auge zu behalten:

1. Sie müssen alle Attribute auflisten, die auf der Instanz gespeichert werden sollen. Wenn Sie ein Attribut vergessen aufzulisten, können Sie es nicht der Instanz zuweisen.
2. Nur die Attribute, die in `__slots__` aufgeführt sind, können Instanzen zugewiesen werden. Dies hilft, eine strenge Struktur für Ihre Objekte zu erzwingen.
3. Instanzen haben keine `__dict__`-Attribute mehr. Da `__slots__` eine statische Struktur erstellt, gibt es keine Notwendigkeit für das dynamische Wörterbuch.
4. Unterklassen erben nicht die `__slots__` ihrer Elternklasse, es sei denn, sie definieren ihre eigenen `__slots__`. Dies bedeutet, dass Unterklassen die Flexibilität haben, ihre eigenen Attributbeschränkungen zu definieren.

Die Hauptvorteile der Verwendung von `__slots__` sind:

1. **Speichereffizienz**: Instanzen verwenden weniger Speicher, da es kein `__dict__` gibt, um Attribute zu speichern.
2. **Geschwindigkeit**: Der Zugriff auf Attribute ist etwas schneller, da Python nicht das Attribut in einem Wörterbuch suchen muss.
3. **Verhinderung versehentlicher Attributerstellung**: Hilft, Tippfehler und Programmierfehler zu erkennen, indem das Hinzufügen unerwarteter Attribute verhindert wird.
