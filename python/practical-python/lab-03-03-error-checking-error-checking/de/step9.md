# Ein etwas besseres Vorgehen

Wenn Sie alle Fehler fangen möchten, ist dies ein vernünftigerer Ansatz.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer sagt nein. Grund :', e)
```

Es meldet einen spezifischen Grund für das Versagen. Es ist fast immer ein guter Gedanke, einen Mechanismus zur Anzeige/Berichterstattung von Fehlern zu haben, wenn Sie Code schreiben, der alle möglichen Ausnahmen fängt.

Im Allgemeinen ist es jedoch besser, die Fehler so eng wie vernünftig zu fangen. Fangen Sie nur die Fehler, die Sie tatsächlich behandeln können. Lassen Sie andere Fehler passieren - vielleicht kann ein anderer Code sie behandeln.
