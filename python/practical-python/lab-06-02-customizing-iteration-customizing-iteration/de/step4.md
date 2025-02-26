# Übung 6.5: Überwachen einer Streaming-Datenquelle

Generatoren können eine interessante Möglichkeit sein, Echtzeit-Datenquellen wie Log-Dateien oder Aktienmärkte zu überwachen. In diesem Teil werden wir diese Idee untersuchen. Beginnen Sie zunächst, indem Sie die folgenden Anweisungen genau befolgen.

Das Programm `stocksim.py` ist ein Programm, das Aktienmarktdaten simuliert. Als Ausgabe schreibt das Programm ständig Echtzeitdaten in eine Datei `stocklog.csv`. Öffnen Sie in einem separaten Befehlsfenster das Verzeichnis und führen Sie dieses Programm aus:

```bash
$ python3 stocksim.py
```

Wenn Sie unter Windows sind, finden Sie einfach die `stocksim.py`-Datei und doppelklicken Sie darauf, um es auszuführen. Vergessen Sie nun dieses Programm (lassen Sie es einfach laufen). Öffnen Sie in einem anderen Fenster die von dem Simulator erstellte Datei `stocklog.csv`. Sie sollten sehen, dass alle paar Sekunden neue Zeilen von Text zur Datei hinzugefügt werden. Lassen Sie dieses Programm ebenfalls im Hintergrund laufen - es wird mehrere Stunden lang laufen (Sie müssen sich nicht darum kümmern).

Wenn das obige Programm läuft, schreiben wir ein kleines Programm, um die Datei zu öffnen, zum Dateiende zu springen und nach neuer Ausgabe zu suchen. Erstellen Sie eine Datei `follow.py` und fügen Sie diesen Code hinzu:

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
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Wenn Sie das Programm ausführen, sehen Sie einen Echtzeit-Aktien-Ticker. Im Hintergrund ähnelt dieser Code der Unix-Befehl `tail -f`, der verwendet wird, um eine Log-Datei zu überwachen.

Hinweis: Die Verwendung der `readline()`-Methode in diesem Beispiel ist etwas ungewöhnlich, da es nicht die übliche Weise ist, Zeilen aus einer Datei zu lesen (normalerweise würden Sie einfach eine `for`-Schleife verwenden). In diesem Fall verwenden wir es jedoch, um wiederholt das Ende der Datei zu überprüfen, um zu sehen, ob weitere Daten hinzugefügt wurden (`readline()` gibt entweder neue Daten oder eine leere Zeichenfolge zurück).
