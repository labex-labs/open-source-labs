# Beenden eines Generators

Eine häufige Frage bezüglich Generatoren betrifft ihre Lebensdauer und die Garbage Collection. Beispielsweise läuft der `follow()`-Generator in einer unendlichen `while`-Schleife für immer. Was passiert, wenn die Iterationsschleife, die ihn antreibt, stoppt? Gibt es außerdem eine Möglichkeit, den Generator vorzeitig zu beenden?

Ändern Sie die `follow()`-Funktion so, dass all den Code in einem `try-except`-Block wie folgt eingeschlossen ist:

```python
def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                 line = f.readline()
                 if line == '':
                     time.sleep(0.1)    # Schlafe kurz, um eine Dauerschleife zu vermeiden
                     continue
                 yield line
    except GeneratorExit:
        print('Following Done')
```

Jetzt führen Sie ein paar Experimente durch:

```python
>>> from follow import follow
>>> # Experiment: Garbage collection eines laufenden Generators
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f
Following Done
>>> # Experiment: Beenden eines Generators
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            f.close()

"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
...
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
        print(line, end='')    # Keine Ausgabe: Der Generator ist beendet

>>>
```

In diesen Experimenten können Sie sehen, dass eine `GeneratorExit`-Ausnahme ausgelöst wird, wenn ein Generator durch die Garbage Collection oder explizit über seine `close()`-Methode geschlossen wird.

Ein weiterer Bereich der Erkundung ist, ob Sie die Iteration bei einem Generator fortsetzen können, wenn Sie aus einer `for`-Schleife ausbrechen. Beispielsweise versuchen Sie dies:

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
...
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> # Iteration fortsetzen
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"AA",39.58,"6/11/2007","09:39.28",-0.08,39.67,39.58,39.31,243159
"HPQ",45.94,"6/11/2007","09:39.29",0.24,45.80,45.94,45.59,408919
...
"IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
>>> del f
Following Done
>>>
```

Im Allgemeinen können Sie aus einer laufenden Iteration ausbrechen und sie später fortsetzen, wenn Sie dies benötigen. Sie müssen nur sicherstellen, dass das Generatorobjekt nicht gewaltsam geschlossen oder irgendwie durch die Garbage Collection entfernt wird.
