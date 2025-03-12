# Praktische Anwendungen der Generatorverwaltung

In diesem Schritt werden wir untersuchen, wie wir die Konzepte, die wir über die Verwaltung von Generatoren und die Behandlung von Ausnahmen in Generatoren gelernt haben, auf reale Szenarien anwenden können. Das Verständnis dieser praktischen Anwendungen wird Ihnen helfen, robusteres und effizienteres Python-Code zu schreiben.

## Erstellen eines robusten Dateiüberwachungssystems

Lassen Sie uns eine zuverlässigere Version unseres Dateiüberwachungssystems erstellen. Dieses System soll in der Lage sein, verschiedene Situationen zu behandeln, wie z. B. Timeouts und Benutzeranforderungen zum Stoppen.

Öffnen Sie zunächst den WebIDE-Editor und erstellen Sie eine neue Datei namens `robust_follow.py`. Hier ist der Code, den Sie in dieser Datei schreiben müssen:

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

In diesem Code definieren wir zunächst eine benutzerdefinierte `TimeoutError`-Klasse. Die Funktion `timeout_handler` wird verwendet, um diese Fehlermeldung auszulösen, wenn ein Timeout auftritt. Die Funktion `follow` ist ein Generator, der eine Datei liest und neue Zeilen ausgibt. Wenn ein Timeout angegeben ist, wird ein Alarm mit dem `signal`-Modul eingerichtet. Wenn es keine neuen Daten in der Datei gibt, wartet es kurz, bevor es es erneut versucht. Der `try - except - finally`-Block wird verwendet, um verschiedene Ausnahmen zu behandeln und eine ordnungsgemäße Aufräumung sicherzustellen.

Nachdem Sie den Code geschrieben haben, speichern Sie die Datei.

## Experimentieren mit dem robusten Dateiüberwachungssystem

Jetzt testen wir unser verbessertes Dateiüberwachungssystem. Öffnen Sie ein Terminal und starten Sie den Python-Interpreter mit den folgenden Befehlen:

```bash
cd ~/project
python3
```

### Experiment 1: Grundlegende Verwendung

Im Python-Interpreter testen wir die grundlegende Funktionalität unseres `follow`-Generators. Hier ist der Code, den Sie ausführen müssen:

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

Hier importieren wir die Funktion `follow` aus unserer `robust_follow.py`-Datei. Dann erstellen wir ein Generatorobjekt `f`, das die `stocklog.csv`-Datei überwacht. Wir verwenden eine `for`-Schleife, um über die vom Generator ausgegebenen Zeilen zu iterieren und die ersten drei Zeilen auszugeben.

### Experiment 2: Verwenden des Timeouts

Lassen Sie uns sehen, wie die Timeout-Funktion funktioniert. Führen Sie den folgenden Code im Python-Interpreter aus:

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

In diesem Experiment erstellen wir einen Generator mit einem 3-Sekunden-Timeout. Wir verarbeiten jede Zeile langsam, indem wir zwischen jeder Zeile 1 Sekunde warten. Nach etwa 3 Sekunden löst der Generator eine Timeout-Ausnahme aus, und der Aufräumcode im `finally`-Block wird ausgeführt.

### Experiment 3: Explizites Schließen

Lassen Sie uns testen, wie der Generator ein explizites Schließen behandelt. Führen Sie den folgenden Code aus:

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

Hier erstellen wir einen Generator und beginnen, über seine Zeilen zu iterieren. Nach der Verarbeitung von zwei Zeilen schließen wir den Generator explizit mit der `close`-Methode. Der Generator behandelt dann die `GeneratorExit`-Ausnahme und führt die erforderliche Aufräumung durch.

## Erstellen einer Datenverarbeitungspipeline mit Fehlerbehandlung

Als Nächstes erstellen wir eine einfache Datenverarbeitungspipeline mit Koroutinen. Diese Pipeline soll in der Lage sein, Fehler in verschiedenen Stadien zu behandeln.

Öffnen Sie den WebIDE-Editor und erstellen Sie eine neue Datei namens `pipeline.py`. Hier ist der Code, den Sie in dieser Datei schreiben müssen:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

In diesem Code wird der `consumer`-Dekorator verwendet, um Koroutinen zu initialisieren. Die Koroutine `grep` filtert Zeilen, die ein bestimmtes Muster enthalten, und sendet sie an eine andere Koroutine. Die Koroutine `printer` gibt die empfangenen Elemente aus. Die Funktion `follow_and_process` liest eine Datei, filtert ihre Zeilen mit der `grep`-Koroutine und gibt die übereinstimmenden Zeilen mit der `printer`-Koroutine aus. Sie behandelt auch die `KeyboardInterrupt`-Ausnahme und stellt eine ordnungsgemäße Aufräumung sicher.

Nachdem Sie den Code geschrieben haben, speichern Sie die Datei.

## Testen der Datenverarbeitungspipeline

Lassen Sie uns unsere Datenverarbeitungspipeline testen. Führen Sie in einem Terminal den folgenden Befehl aus:

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

Diese Ausgabe zeigt, dass die Pipeline korrekt funktioniert und Zeilen filtert und ausgibt, die das "IBM"-Muster enthalten.

Um den Prozess zu stoppen, drücken Sie `Strg+C`. Sie sollten die folgende Nachricht sehen:

```
Processing stopped by user
```

## Wichtige Erkenntnisse

1. Die richtige Behandlung von Ausnahmen in Generatoren ermöglicht es Ihnen, robuste Systeme zu erstellen, die Fehler gracefully behandeln können. Dies bedeutet, dass Ihre Programme nicht unerwartet abstürzen, wenn etwas schief geht.
2. Sie können Techniken wie Timeouts verwenden, um zu verhindern, dass Generatoren unendlich laufen. Dies hilft, Systemressourcen zu verwalten und stellt sicher, dass Ihr Programm nicht in einer Endlosschleife hängen bleibt.
3. Generatoren und Koroutinen können leistungsstarke Datenverarbeitungspipelines bilden, in denen Fehler propagiert und auf der entsprechenden Ebene behandelt werden können. Dies erleichtert es, komplexe Datenverarbeitungssysteme zu erstellen.
4. Der `finally`-Block in Generatoren stellt sicher, dass Aufräumoperationen ausgeführt werden, unabhängig davon, wie der Generator beendet wird. Dies hilft, die Integrität Ihres Programms aufrechtzuerhalten und verhindert Ressourcenlecks.
