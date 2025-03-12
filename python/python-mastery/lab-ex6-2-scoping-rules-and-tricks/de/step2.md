# Verwendung von `locals()` zum Zugriff auf Funktionsargumente

In Python ist das Verständnis von Variablenbereichen (variable scopes) von entscheidender Bedeutung. Der Geltungsbereich einer Variablen bestimmt, wo im Code auf sie zugegriffen werden kann. Python bietet eine eingebaute Funktion namens `locals()`, die für Anfänger sehr nützlich ist, um Geltungsbereiche zu verstehen. Die `locals()`-Funktion gibt ein Wörterbuch zurück, das alle lokalen Variablen im aktuellen Geltungsbereich enthält. Dies kann äußerst nützlich sein, wenn Sie Funktionsargumente untersuchen möchten, da es Ihnen einen klaren Überblick darüber gibt, welche Variablen in einem bestimmten Teil Ihres Codes verfügbar sind.

Lassen Sie uns ein einfaches Experiment im Python-Interpreter durchführen, um zu sehen, wie dies funktioniert. Zunächst müssen wir in das Projektverzeichnis navigieren und den Python-Interpreter starten. Sie können dies tun, indem Sie die folgenden Befehle in Ihrem Terminal ausführen:

```bash
cd ~/project
python3
```

Sobald Sie in der interaktiven Python-Shell sind, werden wir eine `Stock`-Klasse definieren. Eine Klasse in Python ist wie ein Bauplan für die Erstellung von Objekten. In dieser Klasse werden wir die spezielle `__init__`-Methode verwenden. Die `__init__`-Methode ist ein Konstruktor in Python, was bedeutet, dass sie automatisch aufgerufen wird, wenn ein Objekt der Klasse erstellt wird. Innerhalb dieser `__init__`-Methode werden wir die `locals()`-Funktion verwenden, um alle lokalen Variablen auszugeben.

```python
class Stock:
    def __init__(self, name, shares, price):
        print(locals())
```

Jetzt erstellen wir eine Instanz dieser `Stock`-Klasse. Eine Instanz ist ein tatsächliches Objekt, das aus dem Klassenbauplan erstellt wird. Wir werden einige Werte für die Parameter `name`, `shares` und `price` übergeben.

```python
s = Stock('GOOG', 100, 490.1)
```

Wenn Sie diesen Code ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
{'self': <__main__.Stock object at 0x...>, 'name': 'GOOG', 'shares': 100, 'price': 490.1}
```

Diese Ausgabe zeigt, dass `locals()` uns ein Wörterbuch gibt, das alle lokalen Variablen in der `__init__`-Methode enthält. Die `self`-Referenz ist eine spezielle Variable in Python-Klassen, die auf die Instanz der Klasse selbst verweist. Die anderen Variablen sind die Parameterwerte, die wir beim Erstellen des `Stock`-Objekts übergeben haben.

Wir können diese `locals()`-Funktionalität nutzen, um Objektattribute automatisch zu initialisieren. Attribute sind Variablen, die einem Objekt zugeordnet sind. Lassen Sie uns eine Hilfsfunktion definieren und unsere `Stock`-Klasse modifizieren.

```python
def _init(locs):
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init(locals())
```

Die `_init`-Funktion nimmt das Wörterbuch der lokalen Variablen, das von `locals()` erhalten wurde. Sie entfernt zunächst die `self`-Referenz aus dem Wörterbuch mithilfe der `pop`-Methode. Dann iteriert sie über die verbleibenden Schlüssel-Wert-Paare im Wörterbuch und verwendet die `setattr`-Funktion, um jede Variable als Attribut des Objekts festzulegen.

Jetzt testen wir diese Implementierung sowohl mit Positions- als auch mit Schlüsselwortargumenten. Positionsargumente werden in der Reihenfolge übergeben, in der sie in der Funktionssignatur definiert sind, während Schlüsselwortargumente mit den angegebenen Parameternamen übergeben werden.

```python
# Test with positional arguments
s1 = Stock('GOOG', 100, 490.1)
print(s1.name, s1.shares, s1.price)

# Test with keyword arguments
s2 = Stock(name='AAPL', shares=50, price=125.3)
print(s2.name, s2.shares, s2.price)
```

Beide Ansätze sollten jetzt funktionieren! Die `_init`-Funktion ermöglicht es uns, sowohl Positions- als auch Schlüsselwortargumente nahtlos zu verarbeiten. Sie bewahrt auch die Parameternamen in der Funktionssignatur, was die `help()`-Ausgabe nützlicher macht. Die `help()`-Funktion in Python liefert Informationen über Funktionen, Klassen und Module, und wenn die Parameternamen intakt sind, wird diese Information sinnvoller.

Wenn Sie mit dem Experiment fertig sind, können Sie den Python-Interpreter beenden, indem Sie den folgenden Befehl ausführen:

```python
exit()
```
