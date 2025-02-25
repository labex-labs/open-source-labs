# Ausnahmen fangen und behandeln

Ausnahmen können gefangen und behandelt werden.

Um sie zu fangen, verwenden Sie den `try - except`-Befehl.

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
  ...
```

Der Name `ValueError` muss mit der Art des Fehlers übereinstimmen, den Sie fangen möchten.

Es ist oft schwierig, genau vorher zu wissen, welche Arten von Fehlern auftreten können, je nachdem, welche Operation ausgeführt wird. Auf jeden Fall oder auf ungünstige Weise wird die Ausnahmebehandlung oft erst _nachdem_ ein Programm unerwartet abstürzt (z.B. "oh, wir haben vergessen, diesen Fehler zu fangen. Wir sollten das behandeln!").
