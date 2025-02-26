# Übung 6.8: Einfache Pipeline aufsetzen

Schauen wir uns die Pipeline-Idee im Einsatz an. Schreiben Sie die folgende Funktion:

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

Diese Funktion ist fast genau gleich wie das erste Generator-Beispiel aus der vorherigen Übung, nur dass sie keine Datei mehr öffnet, sondern lediglich auf einer Sequenz von Zeilen operiert, die ihr als Argument übergeben werden. Probieren Sie nun Folgendes aus:

```python
>>> from follow import follow
>>> lines = follow('stocklog.csv')
>>> goog = filematch(lines, 'GOOG')
>>> for line in goog:
        print(line)

... warte auf Ausgabe...
```

Es kann einiger Zeit dauern, bis die Ausgabe erscheint, aber schließlich sollten Sie einige Zeilen sehen, die Daten für GOOG enthalten.

Hinweis: Diese Übungen müssen gleichzeitig auf zwei separaten Terminals ausgeführt werden.
