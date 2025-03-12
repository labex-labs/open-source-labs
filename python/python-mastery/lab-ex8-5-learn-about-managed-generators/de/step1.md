# Grundlagen zu Python-Generatoren

Beginnen wir damit, uns zu vergegenwärtigen, was Generatoren in Python sind. In Python sind Generatoren eine besondere Art von Funktion. Sie unterscheiden sich von normalen Funktionen. Wenn Sie eine normale Funktion aufrufen, wird diese von Anfang bis Ende ausgeführt und gibt einen einzelnen Wert zurück. Im Gegensatz dazu gibt eine Generatorfunktion einen Iterator zurück, ein Objekt, über das wir iterieren können, d. h., wir können seine Werte nacheinander abrufen.

Generatoren verwenden die `yield`-Anweisung, um Werte zurückzugeben. Im Gegensatz zu einer normalen Funktion, die alle Werte auf einmal zurückgibt, gibt ein Generator die Werte einzeln zurück. Nachdem ein Generator einen Wert zurückgegeben hat, wird seine Ausführung angehalten. Wenn wir das nächste Mal einen Wert anfordern, wird die Ausführung dort fortgesetzt, wo sie aufgehört hat.

## Erstellen eines einfachen Generators

Jetzt erstellen wir einen einfachen Generator. Im WebIDE müssen Sie eine neue Datei erstellen. Diese Datei wird den Code für unseren Generator enthalten. Benennen Sie die Datei `generator_demo.py` und legen Sie sie im Verzeichnis `/home/labex/project` ab. Hier ist der Inhalt, den Sie in die Datei einfügen sollten:

```python
# Generator function that counts down from n
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Countdown complete!")

# Create a generator object
counter = countdown(5)

# Drive the generator manually
print(next(counter))  # 5
print(next(counter))  # 4
print(next(counter))  # 3

# Iterate through remaining values
for value in counter:
    print(value)  # 2, 1
```

In diesem Code definieren wir zunächst eine Generatorfunktion namens `countdown`. Diese Funktion nimmt eine Zahl `n` als Argument und zählt von `n` bis 1 runter. Innerhalb der Funktion verwenden wir eine `while`-Schleife, um `n` zu dekrementieren und jeden Wert zurückzugeben. Wenn wir `countdown(5)` aufrufen, wird ein Generatorobjekt namens `counter` erstellt.

Anschließend verwenden wir die `next()`-Funktion, um manuell Werte aus dem Generator zu erhalten. Jedes Mal, wenn wir `next(counter)` aufrufen, wird die Ausführung des Generators dort fortgesetzt, wo sie aufgehört hat, und der nächste Wert wird zurückgegeben. Nachdem wir drei Werte manuell abgerufen haben, verwenden wir eine `for`-Schleife, um die verbleibenden Werte im Generator zu durchlaufen.

Um diesen Code auszuführen, öffnen Sie das Terminal und führen Sie den folgenden Befehl aus:

```bash
python3 /home/labex/project/generator_demo.py
```

Wenn Sie den Code ausführen, sollten Sie die folgende Ausgabe sehen:

```
Starting countdown from 5
5
4
3
2
1
Countdown complete!
```

Beachten wir, wie sich die Generatorfunktion verhält:

1. Die Generatorfunktion beginnt ihre Ausführung, wenn wir erstmals `next(counter)` aufrufen. Davor ist die Funktion nur definiert, und es hat noch kein wirkliches Herunterzählen begonnen.
2. Sie pausiert bei jeder `yield`-Anweisung. Nachdem ein Wert zurückgegeben wurde, stoppt sie und wartet auf den nächsten Aufruf von `next()`.
3. Wenn wir `next()` erneut aufrufen, wird die Ausführung dort fortgesetzt, wo sie aufgehört hat. Beispielsweise erinnert sie sich nach dem Zurückgeben von 5 an den Zustand und setzt das Dekrementieren von `n` und das Zurückgeben des nächsten Werts fort.
4. Die Generatorfunktion beendet ihre Ausführung, nachdem der letzte Wert zurückgegeben wurde. In unserem Fall gibt sie nach dem Zurückgeben von 1 "Countdown complete!" aus.

Dieses Vermögen, die Ausführung anzuhalten und fortzusetzen, macht Generatoren so leistungsstark. Es ist sehr nützlich für Aufgaben wie die Task-Scheduling (Aufgabenplanung) und die asynchrone Programmierung, bei denen wir mehrere Aufgaben effizient ausführen müssen, ohne die Ausführung anderer Aufgaben zu blockieren.
