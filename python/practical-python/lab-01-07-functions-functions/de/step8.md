# Übung 1.31: Fehlerbehandlung

Was passiert, wenn Sie Ihre Funktion auf eine Datei mit fehlenden Feldern ausprobieren?

```python
>>> portfolio_cost('missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

An diesem Punkt stehen Sie vor einer Entscheidung. Um das Programm zu machen, können Sie entweder die ursprüngliche Eingabedatei bereinigen, indem Sie schlechte Zeilen eliminieren, oder Sie können Ihren Code so ändern, dass er die schlechten Zeilen auf eine bestimmte Weise behandelt.

Ändern Sie das `pcost.py`-Programm, um die Ausnahme zu fangen, eine Warnmeldung auszugeben und die Verarbeitung der restlichen Datei fortzusetzen.
