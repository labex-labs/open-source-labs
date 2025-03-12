# Messen des Speicherverbrauchs mit verschiedenen Speichermethoden

In diesem Schritt werden wir untersuchen, wie verschiedene Arten der Datenspeicherung den Speicherverbrauch beeinflussen können. Der Speicherverbrauch ist ein wichtiger Aspekt der Programmierung, insbesondere wenn es um große Datensätze geht. Um den Speicherverbrauch unseres Python-Codes zu messen, verwenden wir das `tracemalloc`-Modul von Python. Dieses Modul ist sehr nützlich, da es uns ermöglicht, die von Python vorgenommenen Speicherzuweisungen zu verfolgen. Dadurch können wir sehen, wie viel Speicher unsere Datenspeichermethoden verbrauchen.

## Methode 1: Speichern der gesamten Datei als einzelne Zeichenkette

Beginnen wir damit, eine neue Python-Datei zu erstellen. Navigieren Sie in das Verzeichnis `/home/labex/project` und erstellen Sie eine Datei mit dem Namen `memory_test1.py`. Sie können einen Texteditor verwenden, um diese Datei zu öffnen. Sobald die Datei geöffnet ist, fügen Sie den folgenden Code hinzu. Dieser Code liest den gesamten Inhalt einer Datei als einzelne Zeichenkette und misst den Speicherverbrauch.

```python
# memory_test1.py
import tracemalloc

def test_single_string():
    # Start tracking memory
    tracemalloc.start()

    # Read the entire file as a single string
    with open('/home/labex/project/ctabus.csv') as f:
        data = f.read()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"File length: {len(data)} characters")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_single_string()
```

Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei. Um dieses Skript auszuführen, öffnen Sie Ihr Terminal und geben Sie den folgenden Befehl ein:

```bash
python3 /home/labex/project/memory_test1.py
```

Wenn Sie das Skript ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

Die genauen Zahlen können auf Ihrem System unterschiedlich sein, aber im Allgemeinen werden Sie feststellen, dass der aktuelle Speicherverbrauch etwa 12 MB und der Spitzen-Speicherverbrauch etwa 24 MB beträgt.

## Methode 2: Speichern als Liste von Zeichenketten

Als Nächstes testen wir eine andere Möglichkeit, die Daten zu speichern. Erstellen Sie eine neue Datei mit dem Namen `memory_test2.py` im gleichen Verzeichnis `/home/labex/project`. Öffnen Sie diese Datei im Editor und fügen Sie den folgenden Code hinzu. Dieser Code liest die Datei und speichert jede Zeile als separate Zeichenkette in einer Liste und misst dann den Speicherverbrauch.

```python
# memory_test2.py
import tracemalloc

def test_list_of_strings():
    # Start tracking memory
    tracemalloc.start()

    # Read the file as a list of strings (one string per line)
    with open('/home/labex/project/ctabus.csv') as f:
        lines = f.readlines()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"Number of lines: {len(lines)}")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_list_of_strings()
```

Speichern Sie die Datei und führen Sie dann das Skript mit dem folgenden Befehl im Terminal aus:

```bash
python3 /home/labex/project/memory_test2.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

Beachten Sie, dass der Speicherverbrauch im Vergleich zur vorherigen Methode, die Daten als einzelne Zeichenkette zu speichern, deutlich gestiegen ist. Dies liegt daran, dass jede Zeile in der Liste ein separates Python-Zeichenkettenobjekt ist, und jedes Objekt hat seinen eigenen Speicher-Overhead.

## Verständnis der Speicherdifferenz

Der Unterschied im Speicherverbrauch zwischen den beiden Ansätzen zeigt ein wichtiges Konzept in der Python-Programmierung, das als Objekt-Overhead (engl. object overhead) bezeichnet wird. Wenn Sie Daten als Liste von Zeichenketten speichern, ist jede Zeichenkette ein separates Python-Objekt. Jedes Objekt hat einige zusätzliche Speicheranforderungen, die Folgendes umfassen:

1. Der Python-Objektheader (normalerweise 16 - 24 Bytes pro Objekt). Dieser Header enthält Informationen über das Objekt, wie z. B. seinen Typ und die Referenzzählung.
2. Die eigentliche Zeichenkettenrepräsentation selbst, die die Zeichen der Zeichenkette speichert.
3. Speicherausrichtungsauffüllung (engl. memory alignment padding). Dies ist zusätzlicher Speicherplatz, der hinzugefügt wird, um sicherzustellen, dass die Speicheradresse des Objekts richtig ausgerichtet ist, um einen effizienten Zugriff zu ermöglichen.

Andererseits, wenn Sie den gesamten Dateiinhalt als einzelne Zeichenkette speichern, gibt es nur ein Objekt und somit nur einen Satz von Overhead. Dies macht es bei Betrachtung der Gesamtgröße der Daten speichereffizienter.

Bei der Gestaltung von Programmen, die mit großen Datensätzen arbeiten, müssen Sie diesen Kompromiss zwischen Speichereffizienz und Datenzugänglichkeit berücksichtigen. Manchmal kann es bequemer sein, auf Daten zuzugreifen, wenn sie in einer Liste von Zeichenketten gespeichert sind, aber dies verbraucht mehr Speicher. Andere Male können Sie die Speichereffizienz priorisieren und sich entscheiden, die Daten als einzelne Zeichenkette zu speichern.
