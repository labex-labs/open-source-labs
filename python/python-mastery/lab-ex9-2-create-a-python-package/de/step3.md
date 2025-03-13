# Korrektur der Import-Anweisungen

Jetzt verstehen wir, warum wir dies tun müssen. Als wir unsere Dateien in das `structly`-Paket verschoben haben, hat sich die Art und Weise, wie Python nach Modulen sucht, geändert. Die Import-Anweisungen in jeder Datei müssen aktualisiert werden, um der neuen Paketstruktur zu entsprechen. Dies ist wichtig, da Python diese Import-Anweisungen verwendet, um Code aus anderen Modulen zu finden und zu verwenden.

Die Datei `structure.py` ist besonders wichtig zu aktualisieren. Sie importiert Funktionen und Klassen aus der Datei `validate.py`. Da sich beide Dateien jetzt im gleichen `structly`-Paket befinden, müssen wir die Import-Anweisung entsprechend anpassen.

Beginnen wir damit, die Datei `structly/structure.py` im Editor zu öffnen. Sie können entweder auf `structly/structure.py` im Dateiexplorer klicken oder den folgenden Befehl im Terminal ausführen:

```bash
# Click on structly/structure.py in the file explorer or run:
code structly/structure.py
```

Sobald die Datei geöffnet ist, schauen Sie sich die erste Zeile der Import-Anweisung an. Derzeit sieht sie wie folgt aus:

```python
from validate import validate_type, PositiveInteger, PositiveFloat, String
```

Diese Anweisung war korrekt, als sich die Dateien in einer anderen Struktur befanden. Aber jetzt müssen wir sie ändern, um Python zu sagen, dass es nach dem `validate`-Modul innerhalb desselben Pakets suchen soll. Also ändern wir sie in:

```python
from .validate import validate_type, PositiveInteger, PositiveFloat, String
```

Der Punkt (`.`) vor `validate` ist hier ein wichtiger Bestandteil. Es ist eine spezielle Syntax in Python, die als relativer Import (relative import) bezeichnet wird. Sie sagt Python, dass es nach dem `validate`-Modul im gleichen Paket wie das aktuelle Modul (in diesem Fall `structure.py`) suchen soll.

Nachdem Sie diese Änderung vorgenommen haben, stellen Sie sicher, dass Sie die Datei speichern. Das Speichern ist wichtig, da es die Änderungen dauerhaft macht, und Python die aktualisierte Import-Anweisung verwenden wird, wenn Sie Ihren Code ausführen.

Jetzt überprüfen wir unsere anderen Dateien, um zu sehen, ob sie aktualisiert werden müssen.

1. `structly/reader.py` – Diese Datei importiert nicht aus einem unserer benutzerdefinierten Module. Das bedeutet, dass wir keine Änderungen daran vornehmen müssen.
2. `structly/tableformat.py` – Ähnlich wie die Datei `reader.py` importiert auch diese Datei nicht aus einem unserer benutzerdefinierten Module. Also sind hier ebenfalls keine Änderungen erforderlich.
3. `structly/validate.py` – Genau wie die beiden vorherigen Dateien importiert auch diese nicht aus einem unserer benutzerdefinierten Module. Daher müssen wir sie nicht ändern.

In der Praxis können Ihre Projekte komplexere Beziehungen zwischen Modulen haben. Wenn Sie Dateien verschieben, um eine Paketstruktur zu erstellen oder zu ändern, denken Sie immer daran, die Import-Anweisungen zu aktualisieren. Dies stellt sicher, dass Ihr Code die erforderlichen Module korrekt finden und verwenden kann.
