# Erstellen Ihres ersten Decorators

## Was sind Decorators?

In Python sind Decorators eine besondere Syntax, die für Anfänger sehr nützlich sein kann. Sie ermöglichen es Ihnen, das Verhalten von Funktionen oder Methoden zu ändern. Stellen Sie sich einen Decorator als eine Funktion vor, die eine andere Funktion als Eingabe nimmt. Sie gibt dann eine neue Funktion zurück. Diese neue Funktion erweitert oder ändert oft das Verhalten der ursprünglichen Funktion.

Decorators werden mit dem `@`-Symbol angewendet. Sie platzieren dieses Symbol gefolgt vom Namen des Decorators direkt über einer Funktionsdefinition. Dies ist eine einfache Möglichkeit, Python mitzuteilen, dass Sie den Decorator auf diese bestimmte Funktion anwenden möchten.

## Erstellen eines einfachen Logging-Decorators

Lassen Sie uns einen einfachen Decorator erstellen, der Informationen protokolliert, wenn eine Funktion aufgerufen wird. Logging ist eine häufige Aufgabe in realen Anwendungen, und die Verwendung eines Decorators dafür ist eine gute Möglichkeit, zu verstehen, wie sie funktionieren.

1. Öffnen Sie zunächst den VSCode-Editor. Erstellen Sie im Verzeichnis `/home/labex/project` eine neue Datei mit dem Namen `logcall.py`. In dieser Datei wird unsere Decorator-Funktion gespeichert.

2. Fügen Sie den folgenden Code in `logcall.py` ein:

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Lassen Sie uns analysieren, was dieser Code tut:

- Die `logged`-Funktion ist unser Decorator. Sie nimmt eine andere Funktion, die wir `func` nennen, als Argument. Diese `func` ist die Funktion, für die wir Logging hinzufügen möchten.
- Wenn der Decorator auf eine Funktion angewendet wird, wird eine Nachricht ausgegeben. Diese Nachricht teilt uns mit, dass Logging für die Funktion mit dem angegebenen Namen hinzugefügt wird.
- Innerhalb der `logged`-Funktion definieren wir eine innere Funktion namens `wrapper`. Diese `wrapper`-Funktion wird die ursprüngliche Funktion ersetzen.
  - Wenn die dekorierte Funktion aufgerufen wird, gibt die `wrapper`-Funktion eine Nachricht aus, die besagt, dass die Funktion aufgerufen wird.
  - Sie ruft dann die ursprüngliche Funktion (`func`) mit allen Argumenten auf, die ihr übergeben wurden. Die `*args` und `**kwargs` werden verwendet, um eine beliebige Anzahl von Positions- und Schlüsselwortargumenten zu akzeptieren.
  - Schließlich gibt sie das Ergebnis der ursprünglichen Funktion zurück.
- Die `logged`-Funktion gibt die `wrapper`-Funktion zurück. Diese `wrapper`-Funktion wird jetzt anstelle der ursprünglichen Funktion verwendet und fügt die Logging-Funktionalität hinzu.

## Verwenden des Decorators

3. Erstellen Sie nun im gleichen Verzeichnis (`/home/labex/project`) eine weitere Datei mit dem Namen `sample.py` mit dem folgenden Code:

```python
# sample.py

from logcall import logged

@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y
```

Die `@logged`-Syntax ist hier sehr wichtig. Sie teilt Python mit, den `logged`-Decorator auf die `add`- und `sub`-Funktionen anzuwenden. Wenn also diese Funktionen aufgerufen werden, wird die durch den Decorator hinzugefügte Logging-Funktionalität ausgeführt.

## Testen des Decorators

4. Um Ihren Decorator zu testen, öffnen Sie ein Terminal in VSCode. Ändern Sie zunächst das Verzeichnis in das Projektverzeichnis mit dem folgenden Befehl:

```bash
cd /home/labex/project
```

Starten Sie dann den Python-Interpreter:

```bash
python3
```

5. Importieren Sie im Python-Interpreter das `sample`-Modul und testen Sie die dekorierten Funktionen:

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3, 4)
Calling add
7
>>> sample.sub(2, 3)
Calling sub
-1
>>> exit()
```

Beachten Sie, dass beim Importieren des `sample`-Moduls die Nachrichten "Adding logging to..." ausgegeben werden. Dies liegt daran, dass der Decorator angewendet wird, wenn das Modul importiert wird. Jedes Mal, wenn Sie eine der dekorierten Funktionen aufrufen, wird die "Calling..."-Nachricht ausgegeben. Dies zeigt, dass der Decorator wie erwartet funktioniert.

Dieser einfache Decorator demonstriert das grundlegende Konzept von Decorators. Er umhüllt die ursprüngliche Funktion mit zusätzlicher Funktionalität (in diesem Fall Logging), ohne den Code der ursprünglichen Funktion zu ändern. Dies ist eine leistungsstarke Funktion in Python, die Sie in vielen verschiedenen Szenarien nutzen können.
