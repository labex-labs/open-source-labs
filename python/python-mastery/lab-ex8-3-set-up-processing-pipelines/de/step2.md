# Erstellen von Komponenten für Coroutine-Pipelines

In diesem Schritt werden wir spezialisiertere Coroutinen zur Verarbeitung von Aktiendaten erstellen. Eine Coroutine ist eine spezielle Art von Funktion, die ihre Ausführung anhalten und fortsetzen kann, was für das Aufbauen von Datenverarbeitungspipelines sehr nützlich ist. Jede von uns erstellte Coroutine wird in unserer gesamten Verarbeitungspipeline eine bestimmte Aufgabe ausführen.

1. Zunächst müssen Sie eine neue Datei erstellen. Navigieren Sie zum Verzeichnis `/home/labex/project` und erstellen Sie eine Datei mit dem Namen `coticker.py`. In dieser Datei wird der gesamte Code für unsere auf Coroutinen basierte Datenverarbeitung gespeichert.

2. Jetzt beginnen wir, Code in die Datei `coticker.py` zu schreiben. Zuerst importieren wir die erforderlichen Module und definieren die Grundstruktur. Module sind vorgefertigte Codebibliotheken, die nützliche Funktionen und Klassen bereitstellen. Der folgende Code macht genau das:

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

3. Wenn Sie sich den obigen Code ansehen, werden Sie feststellen, dass es Fehler in Bezug auf `String()`, `Float()` und `Integer()` gibt. Dies sind Klassen, die wir importieren müssen. Daher fügen wir die erforderlichen Importe oben in die Datei ein. Auf diese Weise weiß Python, wo es diese Klassen finden kann. Hier ist der aktualisierte Code:

```python
# coticker.py
from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

4. Als Nächstes fügen wir die Coroutine-Komponenten hinzu, die unsere Datenverarbeitungspipeline bilden werden. Jede Coroutine hat in der Pipeline eine bestimmte Aufgabe. Hier ist der Code, um diese Coroutinen hinzuzufügen:

```python
@consumer
def to_csv(target):
    def producer():
        while True:
            line = yield

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

5. Lassen Sie uns verstehen, was jede dieser Coroutinen tut:

   - `to_csv`: Ihre Aufgabe besteht darin, rohe Textzeilen in geparste CSV-Zeilen umzuwandeln. Dies ist wichtig, da unsere Daten zunächst im Textformat vorliegen und wir sie in strukturierte CSV-Daten aufteilen müssen.
   - `create_ticker`: Diese Coroutine nimmt die CSV-Zeilen und erstellt daraus `Ticker`-Objekte. `Ticker`-Objekte repräsentieren die Aktiendaten auf eine organisiertere Weise.
   - `negchange`: Sie filtert die `Ticker`-Objekte. Sie leitet nur die Aktien weiter, die negative Preisänderungen aufweisen. Dies hilft uns, uns auf die Aktien zu konzentrieren, die an Wert verlieren.
   - `ticker`: Diese Coroutine formatiert und zeigt die Ticker-Daten an. Sie verwendet einen Formatter, um die Daten in einer schönen, lesbaren Tabelle darzustellen.

6. Schließlich müssen wir den Hauptprogrammcode hinzufügen, der alle diese Komponenten miteinander verbindet. Dieser Code wird den Datenfluss durch die Pipeline einrichten. Hier ist der Code:

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change']

    # Create the processing pipeline
    t = ticker('text', fields)
    neg_filter = negchange(t)
    tick_creator = create_ticker(neg_filter)
    csv_parser = to_csv(tick_creator)

    # Connect the pipeline to the data source
    follow('stocklog.csv', csv_parser)
```

7. Nachdem Sie den gesamten Code geschrieben haben, speichern Sie die Datei `coticker.py`. Öffnen Sie dann das Terminal und führen Sie die folgenden Befehle aus. Der `cd`-Befehl wechselt das Verzeichnis zu dem Ort, an dem sich unsere Datei befindet, und der `python3`-Befehl führt unser Python-Skript aus:

```bash
cd /home/labex/project
python3 coticker.py
```

8. Wenn alles gut geht, sollten Sie im Terminal eine formatierte Tabelle sehen. Diese Tabelle zeigt Aktien mit negativen Preisänderungen. Die Ausgabe sieht in etwa so aus:

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

Denken Sie daran, dass die tatsächlichen Werte in der Tabelle je nach generierten Aktiendaten variieren können.

## Das Verständnis des Pipeline-Flusses

Der wichtigste Teil dieses Programms ist, wie Daten durch die Coroutinen fließen. Lassen Sie uns dies Schritt für Schritt aufschlüsseln:

1. Die `follow`-Funktion beginnt damit, Zeilen aus der Datei `stocklog.csv` zu lesen. Dies ist unsere Datenquelle.
2. Jede gelesene Zeile wird dann an die `csv_parser`-Coroutine gesendet. Die `csv_parser` nimmt die rohe Textzeile und parst sie in CSV-Felder.
3. Die geparsten CSV-Daten werden dann an die `tick_creator`-Coroutine gesendet. Diese Coroutine erstellt `Ticker`-Objekte aus den CSV-Zeilen.
4. Die `Ticker`-Objekte werden dann an die `neg_filter`-Coroutine gesendet. Diese Coroutine prüft jedes `Ticker`-Objekt. Wenn die Aktie eine negative Preisänderung aufweist, leitet sie das Objekt weiter; andernfalls verwirft sie es.
5. Schließlich werden die gefilterten `Ticker`-Objekte an die `ticker`-Coroutine gesendet. Die `ticker`-Coroutine formatiert die Daten und zeigt sie in einer Tabelle an.

Diese Pipeline-Architektur ist sehr nützlich, da sie es jeder Komponente ermöglicht, sich auf eine einzelne Aufgabe zu konzentrieren. Dies macht den Code modularer, was bedeutet, dass er leichter zu verstehen, zu ändern und zu warten ist.
