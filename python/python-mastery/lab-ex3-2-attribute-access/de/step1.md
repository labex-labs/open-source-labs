# Das Verständnis des Attributzugriffs in Python

In Python sind Objekte ein grundlegendes Konzept. Sie können Daten in Attributen speichern, die wie benannte Container für Werte sind. Sie können sich Attribute als Variablen vorstellen, die zu einem Objekt gehören. Es gibt mehrere Möglichkeiten, auf diese Attribute zuzugreifen. Die einfachste und am häufigsten verwendete Methode ist die Punktnotation (`.`). Python bietet jedoch auch spezifische Funktionen, die Ihnen mehr Flexibilität beim Umgang mit Attributen geben.

## Die Punktnotation

Beginnen wir damit, ein `Stock`-Objekt zu erstellen und zu sehen, wie wir seine Attribute mithilfe der Punktnotation manipulieren können. Die Punktnotation ist eine einfache und intuitive Möglichkeit, auf die Attribute eines Objekts zuzugreifen und sie zu ändern.

Öffnen Sie zunächst ein neues Terminal und starten Sie die Python interaktive Shell. Hier können Sie Python-Code Zeile für Zeile schreiben und ausführen.

```python
# Open a new terminal and run Python interactive shell
python3

# Import the Stock class from the stock module
from stock import Stock

# Create a Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(s.name)    # Output: 'GOOG'

# Set an attribute
s.shares = 50
print(s.shares)  # Output: 50

# Delete an attribute
del s.shares
# If we try to access s.shares now, we'll get an AttributeError
```

Im obigen Code importieren wir zunächst die `Stock`-Klasse aus dem `stock`-Modul. Dann erstellen wir eine Instanz der `Stock`-Klasse namens `s`. Um den Wert des `name`-Attributs zu erhalten, verwenden wir `s.name`. Um den Wert des `shares`-Attributs zu ändern, weisen wir einfach einen neuen Wert zu `s.shares` zu. Und wenn wir ein Attribut entfernen möchten, verwenden wir das `del`-Schlüsselwort, gefolgt vom Attributnamen.

## Funktionen für den Attributzugriff

Python bietet vier eingebaute Funktionen, die sehr nützlich für die Attributmanipulation sind. Diese Funktionen geben Ihnen mehr Kontrolle beim Umgang mit Attributen, insbesondere wenn Sie sie dynamisch behandeln müssen.

1. `getattr()` – Diese Funktion wird verwendet, um den Wert eines Attributs zu erhalten.
2. `setattr()` – Sie können damit den Wert eines Attributs festlegen.
3. `delattr()` – Mit dieser Funktion können Sie ein Attribut löschen.
4. `hasattr()` – Diese Funktion prüft, ob ein Attribut in einem Objekt existiert.

Sehen wir uns an, wie man diese Funktionen verwendet:

```python
# Create a new Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(getattr(s, 'name'))       # Output: 'GOOG'

# Set an attribute
setattr(s, 'shares', 50)
print(s.shares)                 # Output: 50

# Check if an attribute exists
print(hasattr(s, 'name'))       # Output: True
print(hasattr(s, 'symbol'))     # Output: False

# Delete an attribute
delattr(s, 'shares')
print(hasattr(s, 'shares'))     # Output: False
```

Diese Funktionen sind besonders nützlich, wenn Sie dynamisch mit Attributen arbeiten müssen. Anstatt hartcodierte Attributnamen zu verwenden, können Sie Variablennamen nutzen. Wenn Sie beispielsweise eine Variable haben, die den Namen eines Attributs speichert, können Sie diese Variable an diese Funktionen übergeben, um Operationen auf dem entsprechenden Attribut auszuführen. Dies gibt Ihnen mehr Flexibilität in Ihrem Code, insbesondere wenn Sie auf dynamische Weise mit verschiedenen Objekten und Attributen umgehen.
