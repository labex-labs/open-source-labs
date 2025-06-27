# Import-Anweisungen korrigieren

Lassen Sie uns nun verstehen, warum wir dies tun müssen. Als wir unsere Dateien in das `structly`-Paket verschoben haben, hat sich die Art und Weise, wie Python nach Modulen sucht, geändert. Die Import-Anweisungen in jeder Datei müssen aktualisiert werden, um die neue Paketstruktur abzugleichen. Dies ist entscheidend, da Python diese Import-Anweisungen verwendet, um Code aus anderen Modulen zu finden und zu nutzen.

Die Datei `structure.py` ist sehr wichtig zu aktualisieren. Sie importiert Funktionen und Klassen aus der Datei `validate.py`. Da sich beide Dateien nun im selben `structly`-Paket befinden, müssen wir die Import-Anweisung entsprechend anpassen.

Beginnen wir damit, die Datei `structly/structure.py` im Editor zu öffnen. Sie können entweder in der Dateiexplorer auf `structly/structure.py` klicken oder den folgenden Befehl im Terminal ausführen:

```bash
# Klicken Sie in der Dateiexplorer auf structly/structure.py oder führen Sie aus:
code structly/structure.py
```

Sobald die Datei geöffnet ist, schauen Sie sich die erste Zeile der Import-Anweisung an. Sie sieht derzeit so aus:

```python
from validate import validate_type
```

Diese Anweisung war korrekt, als sich die Dateien in einer anderen Struktur befanden. Aber jetzt müssen wir sie ändern, um Python mitzuteilen, dass es im selben Paket nach dem `validate`-Modul suchen soll. Daher ändern wir sie zu:

```python
from .validate import validate_type
```

Der Punkt (`.`) vor `validate` ist hier ein wichtiger Bestandteil. Es handelt sich um eine spezielle Syntax in Python, die als relativer Import bezeichnet wird. Sie teilt Python mit, im selben Paket wie das aktuelle Modul (in diesem Fall `structure.py`) nach dem `validate`-Modul zu suchen.

Stellen Sie nach dieser Änderung sicher, dass Sie die Datei speichern. Das Speichern ist wichtig, da es die Änderungen dauerhaft macht und Python die aktualisierte Import-Anweisung verwendet, wenn Sie Ihren Code ausführen.

Überprüfen wir nun unsere anderen Dateien, um zu sehen, ob sie Aktualisierungen benötigen.

1. `structly/reader.py` - Diese Datei importiert keine unserer benutzerdefinierten Module. Das bedeutet, dass wir keine Änderungen daran vornehmen müssen.
2. `structly/tableformat.py` - Ähnlich wie die Datei `reader.py` importiert auch diese keine unserer benutzerdefinierten Module. Daher sind hier ebenfalls keine Änderungen erforderlich.
3. `structly/validate.py` - Genau wie die beiden vorherigen Dateien importiert sie keine unserer benutzerdefinierten Module. Daher müssen wir sie nicht ändern.

In der realen Programmierung können Ihre Projekte komplexere Beziehungen zwischen Modulen aufweisen. Wenn Sie Dateien verschieben, um eine Paketstruktur zu erstellen oder zu ändern, denken Sie immer daran, die Import-Anweisungen zu aktualisieren. Dies stellt sicher, dass Ihr Code die notwendigen Module korrekt finden und verwenden kann.
