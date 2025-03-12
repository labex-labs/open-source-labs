# Grundlagen zu Ausnahmen (Exceptions) in Python

In diesem Schritt werden wir uns mit Ausnahmen (Exceptions) in Python befassen. Ausnahmen sind ein wichtiges Konzept in der Programmierung. Sie helfen uns, mit unerwarteten Situationen umzugehen, die während der Ausführung eines Programms auftreten können. Wir werden auch herausfinden, warum der aktuelle Code abstürzt, wenn er versucht, ungültige Daten zu verarbeiten. Das Verständnis dieser Zusammenhänge wird Ihnen helfen, robusteres und zuverlässigeres Python-Code zu schreiben.

## Was sind Ausnahmen?

In Python sind Ausnahmen Ereignisse, die während der Ausführung eines Programms auftreten und den normalen Ablauf der Anweisungen unterbrechen. Stellen Sie sich das wie eine Baustelle auf einer Autobahn vor. Wenn alles reibungslos verläuft, folgt Ihr Programm einem vorgegebenen Pfad, ähnlich wie ein Auto auf einer freien Straße. Wenn jedoch ein Fehler auftritt, erstellt Python ein Ausnahmeobjekt. Dieses Objekt ist wie ein Bericht, der Informationen darüber enthält, was schief gelaufen ist, wie z. B. der Fehlertyp und der Ort im Code, an dem der Fehler aufgetreten ist.

Wenn diese Ausnahmen nicht richtig behandelt werden, führt dies zum Absturz des Programms. Beim Absturz zeigt Python eine Traceback-Nachricht an. Diese Nachricht ist wie eine Karte, die Ihnen den genauen Ort im Code anzeigt, an dem der Fehler aufgetreten ist. Sie ist sehr nützlich für das Debugging.

## Untersuchung des aktuellen Codes

Schauen wir uns zunächst die Struktur der Datei `reader.py` an. Diese Datei enthält Funktionen, die zum Lesen und Konvertieren von CSV-Daten verwendet werden. Um die Datei im Editor zu öffnen, müssen wir in das richtige Verzeichnis navigieren. Wir verwenden dazu den `cd`-Befehl im Terminal.

```bash
cd /home/labex/project
```

Jetzt, da wir im richtigen Verzeichnis sind, schauen wir uns den Inhalt von `reader.py` an. Diese Datei enthält mehrere wichtige Funktionen:

1. `convert_csv()`: Diese Funktion nimmt Datenzeilen entgegen und verwendet eine bereitgestellte Konvertierungsfunktion, um sie zu konvertieren. Sie ist wie eine Maschine, die Rohmaterialien (Datenzeilen) nimmt und sie gemäß einem bestimmten Rezept (der Konvertierungsfunktion) in eine andere Form verwandelt.
2. `csv_as_dicts()`: Diese Funktion liest CSV-Daten und wandelt sie in eine Liste von Wörterbüchern um. Sie führt auch eine Typkonvertierung durch, was bedeutet, dass sie sicherstellt, dass jedes Datenelement im Wörterbuch den richtigen Typ hat, wie z. B. einen String, eine Ganzzahl oder eine Fließkommazahl.
3. `read_csv_as_dicts()`: Dies ist eine Wrapper-Funktion. Sie ist wie ein Manager, der die `csv_as_dicts()`-Funktion aufruft, um die Aufgabe zu erledigen.

## Demonstration des Problems

Schauen wir uns an, was passiert, wenn der Code versucht, ungültige Daten zu verarbeiten. Wir öffnen einen Python-Interpreter, der wie ein Spielplatz ist, auf dem wir unser Python-Code interaktiv testen können. Um den Python-Interpreter zu öffnen, verwenden wir den folgenden Befehl im Terminal:

```bash
python3
```

Sobald der Python-Interpreter geöffnet ist, versuchen wir, die Datei `missing.csv` zu lesen. Diese Datei enthält einige fehlende oder ungültige Daten. Wir verwenden die `read_csv_as_dicts()`-Funktion aus der Datei `reader.py`, um die Daten zu lesen.

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Wenn Sie diesen Code ausführen, sollten Sie eine Fehlermeldung wie diese sehen:

```
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: ''
```

Dieser Fehler tritt auf, weil der Code versucht, einen leeren String in eine Ganzzahl zu konvertieren. Ein leerer String repräsentiert keine gültige Ganzzahl, daher kann Python die Konvertierung nicht durchführen. Die Funktion stürzt beim ersten auftretenden Fehler ab und bricht die Verarbeitung der restlichen gültigen Daten in der Datei ab.

Um den Python-Interpreter zu beenden, geben Sie den folgenden Befehl ein:

```python
exit()
```

## Verständnis des Fehlerablaufs

Der Fehler tritt in der Funktion `convert_csv()` auf, genauer in der folgenden Zeile:

```python
return list(map(lambda row: converter(headers, row), rows))
```

Die `map()`-Funktion wendet die `converter`-Funktion auf jede Zeile in der `rows`-Liste an. Die `converter`-Funktion versucht, die Typen (str, int, float) auf jede Zeile anzuwenden. Wenn sie jedoch auf eine Zeile mit fehlenden Daten stößt, scheitert sie. Die `map()`-Funktion hat keine integrierte Möglichkeit, Ausnahmen zu behandeln. Wenn also eine Ausnahme auftritt, stürzt der gesamte Prozess ab.

Im nächsten Schritt werden Sie den Code so ändern, dass diese Ausnahmen elegant behandelt werden. Dies bedeutet, dass das Programm anstatt abzustürzen in der Lage sein wird, mit den Fehlern umzugehen und die Verarbeitung der restlichen Daten fortzusetzen.
