# Das Verständnis von Coroutinen anhand eines Dateifollowers

Beginnen wir damit, zu verstehen, was Coroutinen sind und wie sie in Python funktionieren. Eine Coroutine ist eine spezialisierte Version einer Generatorfunktion. In Python beginnen Funktionen normalerweise jedes Mal von vorne, wenn sie aufgerufen werden. Coroutinen sind jedoch anders. Sie können sowohl Daten verbrauchen als auch produzieren, und sie haben die Fähigkeit, ihre Ausführung anzuhalten und fortzusetzen. Das bedeutet, dass eine Coroutine ihre Operation an einem bestimmten Punkt anhalten und später genau dort fortsetzen kann, wo sie aufgehört hat.

## Erstellen eines einfachen Dateifollowers mit Coroutinen

In diesem Schritt erstellen wir einen Dateifollower, der Coroutinen verwendet, um eine Datei auf neue Inhalte zu überwachen und diese zu verarbeiten. Dies ähnelt dem Unix-Befehl `tail -f`, der kontinuierlich das Ende einer Datei anzeigt und sich aktualisiert, wenn neue Zeilen hinzugefügt werden.

1. Öffnen Sie den Code-Editor und erstellen Sie eine neue Datei mit dem Namen `cofollow.py` im Verzeichnis `/home/labex/project`. Hier werden wir unseren Python-Code schreiben, um den Dateifollower mit Coroutinen zu implementieren.

2. Kopieren Sie den folgenden Code in die Datei:

```python
# cofollow.py
import os
import time

# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = f.readline()
            if line != '':
                target.send(line)  # Send the line to the target coroutine
            else:
                time.sleep(0.1)  # Sleep briefly if no new content

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)  # Prime the coroutine (necessary first step)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('stocklog.csv', printer())
```

3. Lassen Sie uns die wichtigsten Bestandteile dieses Codes verstehen:
   - `follow(filename, target)`: Diese Funktion ist für das Öffnen einer Datei verantwortlich. Sie bewegt zunächst den Dateizeiger an das Ende der Datei mit `f.seek(0, os.SEEK_END)`. Dann tritt sie in eine Endlosschleife ein, in der sie kontinuierlich versucht, neue Zeilen aus der Datei zu lesen. Wenn eine neue Zeile gefunden wird, sendet sie diese Zeile an die Ziel-Coroutine mit der `send`-Methode. Wenn es keine neuen Inhalte gibt, hält sie kurz (0,1 Sekunden) mit `time.sleep(0.1)` an, bevor sie erneut prüft.
   - `@consumer`-Decorator: In Python müssen Coroutinen "initialisiert" werden, bevor sie Daten empfangen können. Dieser Decorator kümmert sich darum. Er sendet automatisch einen Anfangswert `None` an die Coroutine, was ein notwendiger erster Schritt ist, um die Coroutine für den Empfang echter Daten vorzubereiten.
   - `printer()`-Coroutine: Dies ist eine einfache Coroutine. Sie hat eine Endlosschleife, in der sie das `yield`-Schlüsselwort verwendet, um ein an sie gesendetes Element zu empfangen. Sobald sie ein Element empfängt, gibt sie es einfach aus.

4. Speichern Sie die Datei und führen Sie sie aus dem Terminal aus:

```bash
cd /home/labex/project
python3 cofollow.py
```

5. Sie sollten sehen, dass das Skript den Inhalt der Aktienprotokolldatei ausgibt und weiterhin neue Zeilen ausgibt, wenn sie zur Datei hinzugefügt werden. Drücken Sie `Ctrl+C`, um das Programm zu beenden.

Das Schlüsselkonzept hier ist, dass Daten von der `follow`-Funktion in die `printer`-Coroutine über die `send`-Methode fließen. Diese "Schiebung" von Daten steht im Gegensatz zu Generatoren, die Daten durch Iteration "ziehen". In einem Generator verwenden Sie normalerweise eine `for`-Schleife, um über die von ihm produzierten Werte zu iterieren. In diesem Coroutine-Beispiel werden die Daten jedoch aktiv von einem Teil des Codes an einen anderen gesendet.
