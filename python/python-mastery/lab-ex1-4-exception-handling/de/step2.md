# Hinzufügen von Fehlerbehandlung

Wenn Sie Programme schreiben, die Daten verarbeiten, ist es üblich, Fehler zu finden, die mit schlechten Daten zusammenhängen (fehlerhafte, fehlende Felder usw.). Ändern Sie Ihr `pcost.py`-Programm, um die Daten-Datei `portfolio3.dat` zu lesen und es auszuführen (Hinweis: es sollte abstürzen).

Ändern Sie Ihre Funktion leicht, sodass sie in der Lage ist, von Zeilen mit schlechten Daten wieder aufzunehmen. Beispielsweise werfen die Umwandlungsfunktionen `int()` und `float()` eine `ValueError`-Ausnahme, wenn sie die Eingabe nicht umwandeln können. Verwenden Sie `try` und `except`, um eine Warnmeldung über Zeilen, die nicht analysiert werden können, zu fangen und auszugeben. Beispielsweise:

```shell
Konnte nicht analysieren: 'C - 53,08\n'
Grund: ungültiges Literal für int() mit Basis 10: '-'
Konnte nicht analysieren: 'DIS - 34,20\n'
Grund: ungültiges Literal für int() mit Basis 10: '-'
...
```

Versuchen Sie, Ihr Programm erneut auf die `portfolio3.dat`-Datei auszuführen. Es sollte erfolgreich ausgeführt werden, trotz der ausgegebenen Warnmeldungen.
