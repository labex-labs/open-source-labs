# Verständnis der Lebensdauer und des Schließens von Generatoren

In diesem Schritt werden wir die Lebensdauer von Python-Generatoren untersuchen und lernen, wie wir sie richtig schließen können. Generatoren in Python sind eine spezielle Art von Iteratoren, die es Ihnen ermöglichen, eine Sequenz von Werten on-the-fly zu generieren, anstatt sie alle auf einmal zu berechnen und im Speicher zu speichern. Dies kann sehr nützlich sein, wenn Sie mit großen Datensätzen oder unendlichen Sequenzen arbeiten.

## Was ist der `follow()`-Generator?

Beginnen wir damit, uns die Datei `follow.py` im Projektverzeichnis anzusehen. Diese Datei enthält eine Generatorfunktion namens `follow()`. Eine Generatorfunktion wird wie eine normale Funktion definiert, verwendet jedoch statt des Schlüsselworts `return` das Schlüsselwort `yield`. Wenn eine Generatorfunktion aufgerufen wird, gibt sie ein Generatorobjekt zurück, über das Sie iterieren können, um die von ihr ausgegebenen Werte zu erhalten.

Die Generatorfunktion `follow()` liest kontinuierlich Zeilen aus einer Datei und gibt jede gelesene Zeile aus. Dies ähnelt dem Unix-Befehl `tail -f`, der kontinuierlich eine Datei auf neue Zeilen überwacht.

Öffnen Sie die Datei `follow.py` im WebIDE-Editor:

```python
import os
import time

def follow(filename):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)    # Sleep briefly to avoid busy wait
                continue
            yield line
```

In diesem Code öffnet die Anweisung `with open(filename, 'r') as f` die Datei im Lese-Modus und stellt sicher, dass sie ordnungsgemäß geschlossen wird, wenn der Block verlassen wird. Die Zeile `f.seek(0, os.SEEK_END)` bewegt den Dateizeiger an das Ende der Datei, so dass der Generator am Ende beginnt zu lesen. Die Schleife `while True` liest kontinuierlich Zeilen aus der Datei. Wenn die Zeile leer ist, bedeutet dies, dass es noch keine neuen Zeilen gibt. Daher schläft das Programm für 0,1 Sekunden, um eine Endlosschleife zu vermeiden, und geht dann zur nächsten Iteration über. Wenn die Zeile nicht leer ist, wird sie ausgegeben.

Dieser Generator läuft in einer Endlosschleife, was eine wichtige Frage aufwirft: Was passiert, wenn wir den Generator nicht mehr verwenden oder ihn vorzeitig beenden möchten?

## Modifizieren des Generators zur Behandlung des Schließens

Wir müssen die Funktion `follow()` in `follow.py` modifizieren, um den Fall zu behandeln, wenn der Generator ordnungsgemäß geschlossen wird. Dazu fügen wir einen `try-except`-Block hinzu, der die `GeneratorExit`-Ausnahme fängt. Die `GeneratorExit`-Ausnahme wird ausgelöst, wenn ein Generator geschlossen wird, entweder durch die Garbage Collection oder durch Aufruf der Methode `close()`.

```python
import os
import time

def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)    # Sleep briefly to avoid busy wait
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')
```

In diesem modifizierten Code enthält der `try`-Block die Hauptlogik des Generators. Wenn eine `GeneratorExit`-Ausnahme ausgelöst wird, fängt der `except`-Block sie ab und gibt die Nachricht 'Following Done' aus. Dies ist eine einfache Möglichkeit, Aufräumaktionen durchzuführen, wenn der Generator geschlossen wird.

Speichern Sie die Datei nach diesen Änderungen.

## Experimentieren mit dem Schließen von Generatoren

Jetzt führen wir einige Experimente durch, um zu sehen, wie Generatoren sich verhalten, wenn sie von der Garbage Collection behandelt oder explizit geschlossen werden.

Öffnen Sie ein Terminal und starten Sie den Python-Interpreter:

```bash
cd ~/project
python3
```

### Experiment 1: Garbage Collection eines laufenden Generators

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f  # Delete the generator object
Following Done  # This message appears because of our GeneratorExit handler
```

In diesem Experiment importieren wir zunächst die Funktion `follow` aus der Datei `follow.py`. Dann erstellen wir ein Generatorobjekt `f` durch Aufruf von `follow('stocklog.csv')`. Wir verwenden die Funktion `next()`, um die nächste Zeile aus dem Generator zu erhalten. Schließlich löschen wir das Generatorobjekt mit der Anweisung `del`. Wenn das Generatorobjekt gelöscht wird, wird es automatisch geschlossen, was unseren `GeneratorExit`-Ausnahmehandler auslöst, und die Nachricht 'Following Done' wird ausgegeben.

### Experiment 2: Explizites Schließen eines Generators

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         f.close()  # Explicitly close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
...     print(line, end='')  # No output: generator is closed
...
```

In diesem Experiment erstellen wir ein neues Generatorobjekt `f` und iterieren über es mit einer `for`-Schleife. Innerhalb der Schleife geben wir jede Zeile aus und prüfen, ob die Zeile die Zeichenkette 'IBM' enthält. Wenn dies der Fall ist, rufen wir die Methode `close()` auf dem Generator auf, um ihn explizit zu schließen. Wenn der Generator geschlossen wird, wird die `GeneratorExit`-Ausnahme ausgelöst, und unser Ausnahmehandler gibt die Nachricht 'Following Done' aus. Nachdem der Generator geschlossen wurde, gibt es bei einem erneuten Versuch, über ihn zu iterieren, keine Ausgabe, da der Generator nicht mehr aktiv ist.

### Experiment 3: Abbrechen und Fortsetzen eines Generators

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break  # Break out of the loop, but don't close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
>>> # Resume iteration - the generator is still active
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break
...
"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> del f  # Clean up
Following Done
```

In diesem Experiment erstellen wir ein Generatorobjekt `f` und iterieren über es mit einer `for`-Schleife. Innerhalb der Schleife geben wir jede Zeile aus und prüfen, ob die Zeile die Zeichenkette 'IBM' enthält. Wenn dies der Fall ist, verwenden wir die Anweisung `break`, um aus der Schleife auszubrechen. Das Ausbrechen aus der Schleife schließt den Generator nicht, so dass der Generator noch aktiv ist. Wir können dann die Iteration fortsetzen, indem wir eine neue `for`-Schleife über dasselbe Generatorobjekt starten. Schließlich löschen wir das Generatorobjekt, um aufzuräumen, was unseren `GeneratorExit`-Ausnahmehandler auslöst.

## Wichtige Erkenntnisse

1. Wenn ein Generator geschlossen wird (entweder durch die Garbage Collection oder durch Aufruf von `close()`), wird innerhalb des Generators eine `GeneratorExit`-Ausnahme ausgelöst.
2. Sie können diese Ausnahme fangen, um Aufräumaktionen durchzuführen, wenn der Generator geschlossen wird.
3. Das Ausbrechen aus der Iteration eines Generators (mit `break`) schließt den Generator nicht, so dass er später fortgesetzt werden kann.

Beenden Sie den Python-Interpreter, indem Sie `exit()` eingeben oder `Strg+D` drücken.
