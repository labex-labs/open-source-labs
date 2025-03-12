# Das Verständnis von gebundenen Methoden in Python

In Python sind Methoden ein spezieller Typ von Attributen, die Sie aufrufen können. Wenn Sie eine Methode über ein Objekt zugreifen, erhalten Sie was wir eine "gebundene Methode" nennen. Eine gebundene Methode ist im Wesentlichen eine Methode, die an ein bestimmtes Objekt gebunden ist. Das bedeutet, dass sie auf die Daten des Objekts zugreifen und damit arbeiten kann.

## Der Zugriff auf Methoden als Attribute

Beginnen wir mit der Erkundung von gebundenen Methoden anhand unserer `Stock`-Klasse. Zunächst sehen wir uns an, wie man eine Methode als Attribut eines Objekts zugreift.

```python
# Open a Python interactive shell
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Access the cost method without calling it
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# You can also do this in one step
print(s.cost())  # Output: 49010.0
```

Im obigen Code importieren wir zunächst die `Stock`-Klasse und erstellen eine Instanz davon. Dann greifen wir auf die `cost`-Methode des `s`-Objekts zu, ohne sie tatsächlich aufzurufen. Dadurch erhalten wir eine gebundene Methode. Wenn wir diese gebundene Methode aufrufen, berechnet sie die Kosten basierend auf den Daten des Objekts. Sie können die Methode auch direkt in einem Schritt auf dem Objekt aufrufen.

## Die Verwendung von `getattr()` mit Methoden

Eine andere Möglichkeit, auf Methoden zuzugreifen, ist die Verwendung der `getattr()`-Funktion. Diese Funktion ermöglicht es Ihnen, ein Attribut eines Objekts anhand seines Namens zu erhalten.

```python
# Get the cost method using getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# Get and call in one step
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

Hier verwenden wir `getattr()`, um die `cost`-Methode aus dem `s`-Objekt zu erhalten. Wie zuvor können wir die gebundene Methode aufrufen, um das Ergebnis zu erhalten. Und Sie können die Methode sogar in einer einzigen Zeile erhalten und aufrufen.

## Die gebundene Methode und ihr Objekt

Eine gebundene Methode behält immer einen Verweis auf das Objekt, von dem aus sie zugegriffen wurde. Das bedeutet, dass auch wenn Sie die Methode in einer Variablen speichern, sie noch weiß, zu welchem Objekt sie gehört und auf die Daten des Objekts zugreifen kann.

```python
# Store the cost method in a variable
c = s.cost

# Call the method
print(c())  # Output: 49010.0

# Change the object's state
s.shares = 75

# Call the method again - it sees the updated state
print(c())  # Output: 36757.5
```

In diesem Beispiel speichern wir die `cost`-Methode in einer Variablen `c`. Wenn wir `c()` aufrufen, berechnet es die Kosten basierend auf den aktuellen Daten des Objekts. Dann ändern wir das `shares`-Attribut des `s`-Objekts. Wenn wir `c()` erneut aufrufen, verwendet es die aktualisierten Daten, um die neuen Kosten zu berechnen.

## Die Erkundung der internen Struktur der gebundenen Methode

Eine gebundene Methode hat zwei wichtige Attribute, die uns mehr Informationen über sie geben.

- `__self__`: Dieses Attribut verweist auf das Objekt, an das die Methode gebunden ist.
- `__func__`: Dieses Attribut ist das eigentliche Funktionsobjekt, das die Methode repräsentiert.

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

Hier greifen wir auf die `__self__`- und `__func__`-Attribute der gebundenen Methode `c` zu. Wir können sehen, dass `__self__` das `s`-Objekt ist und `__func__` die `cost`-Funktion. Wir können die Funktion sogar manuell aufrufen, indem wir das Objekt als Argument übergeben, und es gibt uns dasselbe Ergebnis wie der direkte Aufruf der gebundenen Methode.

## Ein Beispiel mit einer Methode, die Argumente nimmt

Sehen wir uns an, wie gebundene Methoden mit einer Methode funktionieren, die Argumente nimmt, wie die `sell()`-Methode.

```python
# Get the sell method
sell_method = s.sell

# Examine the method
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Call the method with an argument
sell_method(25)
print(s.shares)  # Output: 50

# Call the method manually using __func__ and __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

In diesem Beispiel erhalten wir die `sell`-Methode als gebundene Methode. Wenn wir sie mit einem Argument aufrufen, aktualisiert sie das `shares`-Attribut des `s`-Objekts. Wir können die Methode auch manuell unter Verwendung der `__func__`- und `__self__`-Attribute aufrufen und dabei auch das Argument übergeben.

Das Verständnis von gebundenen Methoden hilft Ihnen zu verstehen, wie Python's Objektsystem unter der Haube funktioniert, was für das Debugging, die Metaprogrammierung und das Erstellen fortschrittlicher Programmiermuster nützlich sein kann.
