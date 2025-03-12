# Testen unseres Task-Schedulers

Jetzt werden wir einen Test zu unserer `multitask.py`-Datei hinzufügen. Der Zweck dieses Tests besteht darin, mehrere Aufgaben gleichzeitig auszuführen, was als gleichzeitige Ausführung (concurrent execution) bekannt ist. Die gleichzeitige Ausführung ermöglicht es verschiedenen Aufgaben, scheinbar gleichzeitig Fortschritte zu machen, obwohl in einer single-threaded-Umgebung (eingleitige Umgebung) die Aufgaben tatsächlich abwechselnd ausgeführt werden.

Um diesen Test durchzuführen, fügen Sie den folgenden Code am Ende der `multitask.py`-Datei hinzu:

```python
# Test our scheduler
if __name__ == '__main__':
    # Add tasks to the queue
    tasks.append(countdown(10))  # Count down from 10
    tasks.append(countdown(5))   # Count down from 5
    tasks.append(countup(20))    # Count up to 20

    # Run all tasks
    run()
```

In diesem Code überprüfen wir zunächst, ob das Skript direkt ausgeführt wird, indem wir `if __name__ == '__main__':` verwenden. Dann fügen wir drei verschiedene Aufgaben zur `tasks`-Warteschlange hinzu. Die `countdown`-Aufgaben zählen von den angegebenen Zahlen runter, und die `countup`-Aufgabe zählt bis zur angegebenen Zahl hoch. Schließlich rufen wir die `run()`-Funktion auf, um die Ausführung dieser Aufgaben zu starten.

Nachdem Sie den Code hinzugefügt haben, führen Sie ihn mit dem folgenden Befehl im Terminal aus:

```bash
python3 /home/labex/project/multitask.py
```

Wenn Sie den Code ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen (die genaue Reihenfolge der Zeilen kann variieren):

```
T-minus 10
T-minus 5
Up we go 0
T-minus 9
T-minus 4
Up we go 1
T-minus 8
T-minus 3
Up we go 2
...
```

Beachten Sie, wie die Ausgaben der verschiedenen Aufgaben miteinander vermischt sind. Dies ist ein eindeutiges Zeichen dafür, dass unser Scheduler alle drei Aufgaben gleichzeitig ausführt. Jedes Mal, wenn eine Aufgabe eine `yield`-Anweisung erreicht, pausiert der Scheduler diese Aufgabe und wechselt zu einer anderen, sodass alle Aufgaben im Laufe der Zeit Fortschritte machen können.

## Wie es funktioniert

Schauen wir uns genauer an, was passiert, wenn unser Scheduler läuft:

1. Zunächst fügen wir drei Generator-Aufgaben zur Warteschlange hinzu: `countdown(10)`, `countdown(5)` und `countup(20)`. Diese Generator-Aufgaben sind spezielle Funktionen, die ihre Ausführung an `yield`-Anweisungen anhalten und fortsetzen können.
2. Dann beginnt die `run()`-Funktion ihre Arbeit:
   - Sie nimmt die erste Aufgabe, `countdown(10)`, aus der Warteschlange.
   - Sie führt diese Aufgabe aus, bis sie eine `yield`-Anweisung erreicht. Wenn sie auf die `yield`-Anweisung trifft, gibt sie "T-minus 10" aus.
   - Danach fügt sie die `countdown(10)`-Aufgabe wieder zur Warteschlange hinzu, damit sie später erneut ausgeführt werden kann.
   - Als nächstes nimmt sie die `countdown(5)`-Aufgabe aus der Warteschlange.
   - Sie führt die `countdown(5)`-Aufgabe aus, bis sie auf eine `yield`-Anweisung trifft und gibt "T-minus 5" aus.
   - Und dieser Prozess setzt sich fort...

Dieser Zyklus setzt sich so lange fort, bis alle Aufgaben abgeschlossen sind. Jede Aufgabe bekommt die Chance, für eine kurze Zeit ausgeführt zu werden, was den Eindruck einer gleichzeitigen Ausführung erweckt, ohne dass Threads oder Callbacks verwendet werden müssen. Threads sind eine komplexere Methode, um Parallelität zu erreichen, und Callbacks werden in der asynchronen Programmierung verwendet. Unser einfacher Scheduler verwendet Generatoren, um einen ähnlichen Effekt auf eine einfachere Weise zu erzielen.
