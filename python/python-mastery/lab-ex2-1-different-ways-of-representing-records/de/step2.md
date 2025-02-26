# Grundlegender Speicherbedarf von Text

Lassen Sie uns einen Ausgangspunkt für den Speicherbedarf festlegen, der für diese Datendatei erforderlich ist. Zunächst starten Sie Python neu und führen Sie ein sehr einfaches Experiment durch, indem Sie einfach die Datei aufnehmen und ihre Daten in einem einzigen String speichern:

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('ctabus.csv')
>>> tracemalloc.start()
>>> data = f.read()
>>> len(data)
12361039
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
12369664
>>> peak
24730766
>>>
```

Ihre Ergebnisse können etwas variieren, aber Sie sollten einen aktuellen Speicherbedarf im Bereich von 12 MB mit einem Spitzenwert von 24 MB sehen.

Was passiert, wenn Sie die gesamte Datei stattdessen in eine Liste von Strings lesen? Starten Sie Python neu und versuchen Sie dies:

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('/home/labex/project/ctabus.csv')
>>> tracemalloc.start()
>>> lines = f.readlines()
>>> len(lines)
577564
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
45828030
>>> peak
45867371
>>>
```

Sie sollten sehen, dass der Speicherbedarf erheblich ansteigt und sich im Bereich von 40-50 MB befindet. Etwas, über das nachzudenken ist: was könnte die Quelle dieses zusätzlichen Aufwands sein?
