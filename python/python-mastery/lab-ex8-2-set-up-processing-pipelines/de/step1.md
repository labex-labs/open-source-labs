# Grundlegende Generator-Pipeline mit CSV-Daten

In diesem Schritt lernen wir, wie man mit Generatoren eine grundlegende Verarbeitungspipeline erstellt. Zunächst verstehen wir aber, was Generatoren sind. Generatoren sind eine spezielle Art von Iteratoren in Python. Im Gegensatz zu normalen Iteratoren, die möglicherweise alle Daten auf einmal in den Speicher laden, erzeugen Generatoren Werte bedarfsweise. Dies ist äußerst nützlich, wenn es um große Datenströme geht, da es Speicher spart. Anstatt das gesamte Datenset im Speicher zu speichern, erzeugt der Generator die Werte nacheinander, sobald Sie sie benötigen.

## Verständnis von Generatoren

Ein Generator ist im Wesentlichen eine Funktion, die einen Iterator zurückgibt. Wenn Sie über diesen Iterator iterieren, erzeugt er eine Sequenz von Werten. Die Schreibweise einer Generatorfunktion ähnelt einer normalen Funktion, aber es gibt einen wichtigen Unterschied. Anstelle der `return`-Anweisung verwendet eine Generatorfunktion die `yield`-Anweisung. Die `yield`-Anweisung hat ein einzigartiges Verhalten. Sie pausiert die Funktion und speichert ihren aktuellen Zustand. Wenn der nächste Wert angefordert wird, setzt die Funktion dort fort, wo sie aufgehört hat. Dies ermöglicht es dem Generator, Werte schrittweise zu erzeugen, ohne jedes Mal von vorne beginnen zu müssen.

## Verwendung der `follow()`-Funktion

Die von Ihnen zuvor erstellte `follow()`-Funktion funktioniert ähnlich wie der Unix-Befehl `tail -f`. Der `tail -f`-Befehl überwacht kontinuierlich eine Datei auf neue Inhalte, und das gleiche macht die `follow()`-Funktion. Jetzt verwenden wir sie, um eine einfache Verarbeitungspipeline zu erstellen.

### Schritt 1: Öffnen eines neuen Terminalfensters

Öffnen Sie zunächst ein neues Terminalfenster in der WebIDE. Dies können Sie tun, indem Sie zu `Terminal → New Terminal` gehen. In diesem neuen Terminal werden wir unsere Python-Befehle ausführen.

### Schritt 2: Starten einer interaktiven Python-Shell

Sobald das neue Terminal geöffnet ist, starten Sie eine interaktive Python-Shell. Dies können Sie tun, indem Sie den folgenden Befehl im Terminal eingeben:

```bash
python3
```

Die interaktive Python-Shell ermöglicht es Ihnen, Python-Code zeilenweise auszuführen und die Ergebnisse sofort zu sehen.

### Schritt 3: Importieren der `follow`-Funktion und Einrichten der Pipeline

Jetzt importieren wir die `follow`-Funktion und richten eine grundlegende Pipeline ein, um die Aktiendaten zu lesen. Geben Sie in der interaktiven Python-Shell den folgenden Code ein:

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
...     print(row)
...
```

Hier ist, was jede Zeile tut:

- `from follow import follow`: Dies importiert die `follow`-Funktion aus dem `follow`-Modul.
- `import csv`: Dies importiert das `csv`-Modul, das in Python zum Lesen und Schreiben von CSV-Dateien verwendet wird.
- `lines = follow('stocklog.csv')`: Dies ruft die `follow`-Funktion mit dem Dateinamen `stocklog.csv` auf. Die `follow`-Funktion gibt einen Generator zurück, der neue Zeilen liefert, sobald sie zur Datei hinzugefügt werden.
- `rows = csv.reader(lines)`: Die `csv.reader()`-Funktion nimmt die von der `follow`-Funktion erzeugten Zeilen und parst sie in CSV-Datenzeilen.
- Die `for`-Schleife iteriert über diese Zeilen und gibt jede Zeile aus.

### Schritt 4: Überprüfen der Ausgabe

Nachdem Sie den Code ausgeführt haben, sollten Sie eine Ausgabe ähnlich der folgenden sehen (Ihre Daten werden variieren):

```
['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Diese Ausgabe zeigt, dass Sie erfolgreich eine Datenpipeline erstellt haben. Die `follow()`-Funktion erzeugt Zeilen aus der Datei, und diese Zeilen werden dann an die `csv.reader()`-Funktion übergeben, die sie in Datenzeilen parst.

Wenn Sie genug Ausgabe gesehen haben, können Sie die Ausführung durch Drücken von `Ctrl+C` stoppen.

## Was passiert hier?

Lassen Sie uns analysieren, was in dieser Pipeline passiert:

1. `follow('stocklog.csv')` erstellt einen Generator. Dieser Generator verfolgt die Datei `stocklog.csv` und liefert neue Zeilen, sobald sie zur Datei hinzugefügt werden.
2. `csv.reader(lines)` nimmt die von der `follow`-Funktion erzeugten Zeilen und parst sie in CSV-Zeildaten. Sie versteht die Struktur von CSV-Dateien und teilt die Zeilen in einzelne Werte auf.
3. Die `for`-Schleife iteriert dann über diese Zeilen und gibt jede Zeile aus. Dies ermöglicht es Ihnen, die Daten in einem lesbaren Format zu sehen.

Dies ist ein einfaches Beispiel für eine Datenverarbeitungspipeline mit Generatoren. In den nächsten Schritten werden wir komplexere und nützlichere Pipelines erstellen.
