# Das Problem bei der Klasseninitialisierung verstehen

In der Welt der Programmierung sind Klassen ein grundlegendes Konzept, das es Ihnen ermöglicht, benutzerdefinierte Datentypen zu erstellen. In früheren Übungen haben Sie möglicherweise eine `Structure`-Klasse erstellt. Diese Klasse ist ein nützliches Werkzeug, um Datenstrukturen einfach zu definieren. Eine Datenstruktur ist eine Möglichkeit, Daten zu organisieren und zu speichern, damit sie effizient abgerufen und verwendet werden können. Die `Structure`-Klasse als Basisklasse kümmert sich um die Initialisierung von Attributen anhand einer vordefinierten Liste von Feldnamen. Attribute sind Variablen, die zu einem Objekt gehören, und Feldnamen sind die Namen, die wir diesen Attributen geben.

Schauen wir uns die aktuelle Implementierung der `Structure`-Klasse genauer an. Dazu müssen wir die Datei `structure.py` im Code-Editor öffnen. Diese Datei enthält den Code für die `Structure`-Klasse. Hier sind die Befehle, um in das Projektverzeichnis zu navigieren und die Datei zu öffnen:

```bash
cd ~/project
code structure.py
```

Die `Structure`-Klasse bietet einen grundlegenden Rahmen für die Definition einfacher Datenstrukturen. Wenn wir eine Unterklasse wie die `Stock`-Klasse erstellen, können wir die spezifischen Felder definieren, die wir für diese Unterklasse benötigen. Eine Unterklasse erbt die Eigenschaften und Methoden ihrer Basisklasse, in diesem Fall die `Structure`-Klasse. Beispielsweise definieren wir in der `Stock`-Klasse die Felder `name`, `shares` und `price`:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')
```

Jetzt öffnen wir die Datei `stock.py`, um zu sehen, wie die `Stock`-Klasse im Kontext des gesamten Codes implementiert ist. Diese Datei enthält wahrscheinlich den Code, der die `Stock`-Klasse verwendet und mit ihr interagiert. Verwenden Sie den folgenden Befehl, um die Datei zu öffnen:

```bash
code stock.py
```

Obwohl dieser Ansatz mit der `Structure`-Klasse und ihren Unterklassen funktioniert, hat er mehrere Einschränkungen. Um diese Probleme zu identifizieren, werden wir den Python-Interpreter starten und untersuchen, wie die `Stock`-Klasse verhält. Der folgende Befehl importiert die `Stock`-Klasse und zeigt ihre Hilfsinformationen an:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Wenn Sie diesen Befehl ausführen, werden Sie feststellen, dass die im Hilfsoutput angezeigte Signatur nicht sehr hilfreich ist. Anstelle der tatsächlichen Parameternamen wie `name`, `shares` und `price` wird nur `*args` angezeigt. Dieser Mangel an klaren Parameternamen macht es für Benutzer schwierig, zu verstehen, wie sie korrekt eine Instanz der `Stock`-Klasse erstellen können.

Versuchen wir auch, eine `Stock`-Instanz mit Schlüsselwortargumenten zu erstellen. Schlüsselwortargumente ermöglichen es Ihnen, die Werte für Parameter anhand ihrer Namen anzugeben, was den Code lesbarer machen kann. Führen Sie den folgenden Befehl aus:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Sie sollten eine Fehlermeldung wie diese erhalten:

```
TypeError: __init__() got an unexpected keyword argument 'name'
```

Dieser Fehler tritt auf, weil unsere aktuelle `__init__`-Methode, die für die Initialisierung von Objekten der `Stock`-Klasse verantwortlich ist, keine Schlüsselwortargumente verarbeitet. Sie akzeptiert nur Positionsargumente, was bedeutet, dass Sie die Werte in einer bestimmten Reihenfolge angeben müssen, ohne die Parameternamen zu verwenden. Dies ist eine Einschränkung, die wir in diesem Lab beheben möchten.

In diesem Lab werden wir verschiedene Ansätze untersuchen, um unsere `Structure`-Klasse flexibler und benutzerfreundlicher zu machen. Dadurch können wir die Benutzerfreundlichkeit der `Stock`-Klasse und anderer Unterklassen von `Structure` verbessern.
