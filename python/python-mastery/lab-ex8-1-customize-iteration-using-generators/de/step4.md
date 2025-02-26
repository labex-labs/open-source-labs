# Überwachen einer Streaming-Datenquelle

Generatoren können auch eine nützliche Möglichkeit sein, einfach einen Datenstrom zu erzeugen. In diesem Teil werden wir diese Idee erkunden, indem wir einen Generator schreiben, um eine Logdatei zu überwachen. Beginnen Sie zunächst mit den folgenden Anweisungen.

Das Programm `stocksim.py` ist ein Programm, das die Aktienmarkt-Daten simuliert. Als Ausgabe schreibt das Programm kontinuierlich Echtzeitdaten in eine Datei `stocklog.csv`. Öffnen Sie in einem Befehlsfenster (nicht IDLE) das Verzeichnis und führen Sie dieses Programm aus:

    % python3 stocksim.py

Wenn Sie unter Windows sind, finden Sie einfach die `stocksim.py`-Datei und doppelklicken Sie darauf, um es auszuführen. Vergessen Sie jetzt dieses Programm (lassen Sie es einfach laufen). Lassen Sie dieses Programm einfach im Hintergrund laufen - es wird mehrere Stunden lang laufen (Sie müssen sich nicht darum kümmern).

Wenn das obige Programm läuft, schreiben wir ein kleines Programm, um die Datei zu öffnen, zum Dateiende zu springen und nach neuer Ausgabe zu suchen. Erstellen Sie eine Datei `follow.py` und legen Sie diesen Code darin ab:

```python
# follow.py
import os
import time
f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Bewege den Dateizeiger um 0 Bytes vom Dateiende
while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Schlafe kurz und versuche es erneut
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

Wenn Sie das Programm ausführen, sehen Sie einen Echtzeit-Aktienanzeiger. Unter der Haube ist dieser Code ähnlich der Unix-Befehl `tail -f`, der verwendet wird, um eine Logdatei zu überwachen.

**Hinweis:** Die Verwendung der `readline()`-Methode in diesem Beispiel ist etwas ungewöhnlich, da es nicht die übliche Weise ist, Zeilen aus einer Datei zu lesen (normalerweise würden Sie einfach eine `for`-Schleife verwenden). In diesem Fall verwenden wir es jedoch, um wiederholt das Ende der Datei zu überprüfen, um zu sehen, ob weitere Daten hinzugefügt wurden (`readline()` wird entweder neue Daten oder eine leere Zeichenfolge zurückgeben).

Wenn Sie sich den Code genauer ansehen, produziert der erste Teil des Codes Zeilen von Daten, während die Anweisungen am Ende der `while`-Schleife die Daten verarbeiten. Ein wichtiges Merkmal von Generatorfunktionen ist, dass Sie den gesamten Datenproduktionscode in eine wiederverwendbare Funktion verschieben können.

Ändern Sie den Code so, dass das Datei-Lesen von einer Generatorfunktion `follow(filename)` durchgeführt wird. Stellen Sie sicher, dass der folgende Code funktioniert:

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Sollte hier Zeilen der Ausgabe sehen...
```

Ändern Sie den Aktienanzeiger-Code so, dass er wie folgt aussieht:

```python
for line in follow('stocklog.csv'):
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

**Diskussion**

Etwas sehr Potentes ist gerade passiert. Sie haben ein interessantes Iterationsmuster (Lesen von Zeilen am Ende einer Datei) in seine eigene kleine Funktion verlagert. Die `follow()`-Funktion ist jetzt eine völlig allzweckdienliche Utility, die Sie in jedem Programm verwenden können. Beispielsweise können Sie sie verwenden, um Server-Logs, Debug-Logs und andere ähnliche Datenquellen zu überwachen. Das ist ziemlich cool.
