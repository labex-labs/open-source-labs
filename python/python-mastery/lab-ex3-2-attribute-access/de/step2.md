# Die Verwendung von `getattr()` für die generische Objektverarbeitung

Die `getattr()`-Funktion ist ein leistungsstarkes Werkzeug in Python, das es Ihnen ermöglicht, auf die Attribute eines Objekts auf dynamische Weise zuzugreifen. Dies ist besonders nützlich, wenn Sie Objekte auf eine generische Weise verarbeiten möchten. Anstatt Code zu schreiben, der für einen bestimmten Objekttyp spezifisch ist, können Sie `getattr()` verwenden, um mit jedem Objekt zu arbeiten, das die erforderlichen Attribute hat. Diese Flexibilität macht Ihren Code wiederverwendbarer und anpassungsfähiger.

## Die Verarbeitung mehrerer Attribute

Beginnen wir damit, zu lernen, wie man mithilfe der `getattr()`-Funktion auf mehrere Attribute eines Objekts zugreift. Dies ist ein häufiges Szenario, wenn Sie bestimmte Informationen aus einem Objekt extrahieren müssen.

Öffnen Sie zunächst die Python interaktive Shell, wenn Sie die vorherige geschlossen haben. Sie können dies tun, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```python
# Open a Python interactive shell if you closed the previous one
python3
```

Als Nächstes werden wir die `Stock`-Klasse importieren und ein `Stock`-Objekt erstellen. Die `Stock`-Klasse repräsentiert eine Aktie mit Attributen wie `name`, `shares` und `price`.

```python
# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.1)
```

Jetzt definieren wir eine Liste von Attributnamen, auf die wir zugreifen möchten. Diese Liste wird uns helfen, über die Attribute zu iterieren und ihre Werte auszugeben.

```python
# Define a list of attribute names
fields = ['name', 'shares', 'price']
```

Schließlich verwenden wir eine `for`-Schleife, um über die Liste der Attributnamen zu iterieren und auf jedes Attribut mithilfe von `getattr()` zuzugreifen. Wir geben für jede Iteration den Attributnamen und seinen Wert aus.

```python
# Access each attribute using getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

Wenn Sie diesen Code ausführen, sehen Sie die folgende Ausgabe:

```
name: GOOG
shares: 100
price: 490.1
```

Diese Ausgabe zeigt, dass wir in der Lage waren, die Werte mehrerer Attribute des `Stock`-Objekts mithilfe der `getattr()`-Funktion zuzugreifen und auszugeben.

## Standardwerte mit `getattr()`

Die `getattr()`-Funktion bietet auch ein nützliches Feature: die Möglichkeit, einen Standardwert anzugeben, wenn das Attribut, auf das Sie zugreifen möchten, nicht existiert. Dies kann verhindern, dass Ihr Code einen `AttributeError` auslöst und ihn robuster machen.

Sehen wir uns an, wie dies funktioniert. Zunächst versuchen wir, auf ein Attribut zuzugreifen, das im `Stock`-Objekt nicht existiert. Wir verwenden `getattr()` und geben einen Standardwert von `'N/A'` an.

```python
# Try to access an attribute that doesn't exist
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'
```

In diesem Fall, da das `symbol`-Attribut im `Stock`-Objekt nicht existiert, gibt `getattr()` den Standardwert `'N/A'` zurück.

Jetzt vergleichen wir dies mit dem Zugriff auf ein vorhandenes Attribut. Wir greifen auf das `name`-Attribut zu, das im `Stock`-Objekt existiert.

```python
# Compare with an existing attribute
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

Hier gibt `getattr()` den tatsächlichen Wert des `name`-Attributs zurück, der `'GOOG'` ist.

## Die Verarbeitung einer Sammlung von Objekten

Die `getattr()`-Funktion wird noch leistungsstärker, wenn Sie eine Sammlung von Objekten verarbeiten müssen. Sehen wir uns an, wie wir sie verwenden können, um ein Portfolio von Aktien zu verarbeiten.

Zunächst importieren wir die `read_portfolio`-Funktion aus dem `stock`-Modul. Diese Funktion liest ein Portfolio von Aktien aus einer CSV-Datei und gibt eine Liste von `Stock`-Objekten zurück.

```python
# Import the portfolio reading function
from stock import read_portfolio
```

Als Nächstes verwenden wir die `read_portfolio`-Funktion, um das Portfolio aus einer CSV-Datei namens `portfolio.csv` zu lesen.

```python
# Read the portfolio from CSV file
portfolio = read_portfolio('portfolio.csv')
```

Schließlich verwenden wir eine `for`-Schleife, um über die Liste der `Stock`-Objekte im Portfolio zu iterieren. Für jede Aktie verwenden wir `getattr()`, um auf die `name`- und `shares`-Attribute zuzugreifen und ihre Werte auszugeben.

```python
# Print the name and shares of each stock
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

Dieser Ansatz macht Ihren Code flexibler, da Sie mit Attributnamen als Strings arbeiten können. Diese Strings können als Argumente übergeben oder in Datenstrukturen gespeichert werden, sodass Sie die Attribute, auf die Sie zugreifen möchten, leicht ändern können, ohne die Kernlogik Ihres Codes zu ändern.
