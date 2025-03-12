# Erstellen eines Generators für Streaming-Daten

In der Programmierung sind Generatoren ein leistungsstarkes Werkzeug, insbesondere wenn es um reale Probleme wie die Überwachung einer Streaming-Datenquelle geht. In diesem Abschnitt lernen wir, wie wir das, was wir über Generatoren gelernt haben, auf ein solches praktisches Szenario anwenden können. Wir werden einen Generator erstellen, der eine Protokolldatei (Log-Datei) überwacht und uns neue Zeilen liefert, sobald sie zur Datei hinzugefügt werden.

## Einrichten der Datenquelle

Bevor wir mit der Erstellung des Generators beginnen, müssen wir eine Datenquelle einrichten. In diesem Fall verwenden wir ein Simulationsprogramm, das Börsendaten generiert.

Zunächst müssen Sie ein neues Terminal in der WebIDE öffnen. Hier werden Sie die Befehle ausführen, um die Simulation zu starten.

Nachdem Sie das Terminal geöffnet haben, führen Sie das Börsensimulationsprogramm aus. Hier sind die Befehle, die Sie eingeben müssen:

```bash
cd ~/project
python3 stocksim.py
```

Der erste Befehl `cd ~/project` wechselt das aktuelle Verzeichnis in das `project`-Verzeichnis in Ihrem Home-Verzeichnis. Der zweite Befehl `python3 stocksim.py` führt das Börsensimulationsprogramm aus. Dieses Programm generiert Börsendaten und schreibt sie in eine Datei namens `stocklog.csv` im aktuellen Verzeichnis. Lassen Sie dieses Programm im Hintergrund laufen, während wir an dem Überwachungscode arbeiten.

## Erstellen eines einfachen Datei-Überwachers

Jetzt, da wir unsere Datenquelle eingerichtet haben, erstellen wir ein Programm, das die Datei `stocklog.csv` überwacht. Dieses Programm zeigt alle negativen Preisänderungen an.

1. Erstellen Sie zunächst eine neue Datei namens `follow.py` in der WebIDE. Dazu müssen Sie das Verzeichnis in das `project`-Verzeichnis wechseln, indem Sie den folgenden Befehl im Terminal eingeben:

```bash
cd ~/project
```

2. Fügen Sie als Nächstes den folgenden Code zur Datei `follow.py` hinzu. Dieser Code öffnet die Datei `stocklog.csv`, bewegt den Dateizeiger an das Ende der Datei und überprüft dann kontinuierlich auf neue Zeilen. Wenn eine neue Zeile gefunden wird und sie eine negative Preisänderung darstellt, wird der Name der Aktie, der Preis und die Änderung ausgegeben.

```python
# follow.py
import os
import time

f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

3. Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei. Führen Sie dann das Programm aus, indem Sie den folgenden Befehl im Terminal eingeben:

```bash
python3 follow.py
```

Sie sollten eine Ausgabe sehen, die Aktien mit negativen Preisänderungen anzeigt. Es könnte so aussehen:

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

Wenn Sie das Programm beenden möchten, drücken Sie `Ctrl+C` im Terminal.

## Umwandlung in eine Generatorfunktion

Obwohl der vorherige Code funktioniert, können wir ihn wiederverwendbarer und modularer gestalten, indem wir ihn in eine Generatorfunktion umwandeln. Eine Generatorfunktion ist eine spezielle Art von Funktion, die angehalten und fortgesetzt werden kann und die nacheinander Werte liefert.

1. Öffnen Sie die Datei `follow.py` erneut und ändern Sie sie so, dass eine Generatorfunktion verwendet wird. Hier ist der aktualisierte Code:

```python
# follow.py
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file as they are added.
    Similar to the 'tail -f' Unix command.
    """
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move to the end of the file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example usage - monitor stocks with negative price changes
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

Die `follow`-Funktion ist jetzt eine Generatorfunktion. Sie öffnet die Datei, bewegt sich an das Ende und überprüft dann kontinuierlich auf neue Zeilen. Wenn eine neue Zeile gefunden wird, liefert sie diese Zeile.

2. Speichern Sie die Datei und führen Sie sie erneut aus, indem Sie den Befehl eingeben:

```bash
python3 follow.py
```

Die Ausgabe sollte die gleiche wie zuvor sein. Aber jetzt ist die Logik zur Dateiüberwachung sauber in der `follow`-Generatorfunktion gekapselt. Dies bedeutet, dass wir diese Funktion in anderen Programmen wiederverwenden können, die eine Datei überwachen müssen.

## Verständnis der Stärke von Generatoren

Durch die Umwandlung unseres Dateilesecodes in eine Generatorfunktion haben wir ihn viel flexibler und wiederverwendbarer gemacht. Die `follow()`-Funktion kann in jedem Programm verwendet werden, das eine Datei überwachen muss, nicht nur für Börsendaten.

Beispielsweise könnten Sie sie verwenden, um Serverprotokolle, Anwendungslogs oder jede andere Datei zu überwachen, die im Laufe der Zeit aktualisiert wird. Dies zeigt, wie Generatoren eine großartige Möglichkeit sind, Streaming-Datenquellen auf saubere und modulare Weise zu verarbeiten.
