# Steuerung exportierter Symbole mit `__all__`

In Python möchten Sie möglicherweise steuern, welche Symbole (Funktionen, Klassen, Variablen) aus einem Modul importiert werden, wenn Sie die Anweisung `from module import *` verwenden. Hier kommt die Variable `__all__` zum Einsatz. Die Anweisung `from module import *` ist eine Möglichkeit, alle Symbole aus einem Modul in den aktuellen Namensraum zu importieren. Manchmal möchten Sie jedoch nicht jedes einzelne Symbol importieren, insbesondere wenn es viele gibt oder wenn einige für die interne Verwendung im Modul gedacht sind. Die Variable `__all__` ermöglicht es Ihnen, genau anzugeben, welche Symbole bei Verwendung dieser Anweisung importiert werden sollen.

## Was ist `__all__`?

Die Variable `__all__` ist eine Liste von Strings. Jeder String in dieser Liste repräsentiert ein Symbol (Funktion, Klasse oder Variable), das ein Modul exportiert, wenn jemand die Anweisung `from module import *` verwendet. Wenn die Variable `__all__` in einem Modul nicht definiert ist, wird die Anweisung `import *` alle Symbole importieren, die nicht mit einem Unterstrich beginnen. Symbole, die mit einem Unterstrich beginnen, werden normalerweise als privat oder intern für das Modul angesehen und sollen nicht direkt importiert werden.

## Modifizieren jedes Untermoduls

Jetzt fügen wir die Variable `__all__` zu jedem Untermodul im `structly`-Paket hinzu. Dies hilft uns, zu steuern, welche Symbole aus jedem Untermodul exportiert werden, wenn jemand die Anweisung `from module import *` verwendet.

1. Zunächst modifizieren wir `structure.py`:

```bash
touch ~/project/structly/structure.py
```

Dieser Befehl erstellt eine neue Datei namens `structure.py` im `structly`-Verzeichnis Ihres Projekts. Nach dem Erstellen der Datei müssen wir die Variable `__all__` hinzufügen. Fügen Sie diese Zeile ganz oben in die Datei, direkt nach den Importanweisungen, ein:

```python
__all__ = ['Structure']
```

Diese Zeile teilt Python mit, dass nur das Symbol `Structure` importiert wird, wenn jemand `from structure import *` verwendet. Speichern Sie die Datei und verlassen Sie den Editor.

2. Als Nächstes modifizieren wir `reader.py`:

```bash
touch ~/project/structly/reader.py
```

Dieser Befehl erstellt eine neue Datei namens `reader.py` im `structly`-Verzeichnis. Durchsuchen Sie nun die Datei, um alle Funktionen zu finden, die mit `read_csv_as_` beginnen. Diese Funktionen sind diejenigen, die wir exportieren möchten. Fügen Sie dann eine `__all__`-Liste mit allen diesen Funktionsnamen hinzu. Sie sollte in etwa so aussehen:

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

Beachten Sie, dass die tatsächlichen Funktionsnamen je nach Inhalt der Datei variieren können. Stellen Sie sicher, dass Sie alle `read_csv_as_*`-Funktionen, die Sie finden, einschließen. Speichern Sie die Datei und verlassen Sie den Editor.

3. Jetzt modifizieren wir `tableformat.py`:

```bash
touch ~/project/structly/tableformat.py
```

Dieser Befehl erstellt eine neue Datei namens `tableformat.py` im `structly`-Verzeichnis. Fügen Sie diese Zeile ganz oben in die Datei ein:

```python
__all__ = ['create_formatter', 'print_table']
```

Diese Zeile gibt an, dass nur die Symbole `create_formatter` und `print_table` importiert werden, wenn jemand `from tableformat import *` verwendet. Speichern Sie die Datei und verlassen Sie den Editor.

## Einheitliche Imports in `__init__.py`

Jetzt, da jedes Modul definiert, was es exportiert, können wir die `__init__.py`-Datei aktualisieren, um alle diese Symbole zu importieren. Die `__init__.py`-Datei ist eine besondere Datei in Python-Paketen. Sie wird ausgeführt, wenn das Paket importiert wird, und kann verwendet werden, um das Paket zu initialisieren und Symbole aus Untermodulen zu importieren.

```bash
touch ~/project/structly/__init__.py
```

Dieser Befehl erstellt eine neue `__init__.py`-Datei im `structly`-Verzeichnis. Ändern Sie den Inhalt der Datei wie folgt:

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

Diese Zeilen importieren alle exportierten Symbole aus den Untermodulen `structure`, `reader` und `tableformat`. Der Punkt (`.`) vor den Modulnamen gibt an, dass es sich um relative Imports handelt, d. h. Imports aus dem gleichen Paket. Speichern Sie die Datei und verlassen Sie den Editor.

## Testen unserer Änderungen

Erstellen wir eine einfache Testdatei, um zu überprüfen, ob unsere Änderungen funktionieren. Diese Testdatei versucht, die Symbole zu importieren, die wir in den `__all__`-Variablen angegeben haben, und gibt eine Erfolgsmeldung aus, wenn die Imports erfolgreich sind.

```bash
touch ~/project/test_structly.py
```

Dieser Befehl erstellt eine neue Datei namens `test_structly.py` im Projektverzeichnis. Fügen Sie den folgenden Inhalt in die Datei ein:

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

Diese Zeilen versuchen, die Klasse `Structure`, die Funktion `read_csv_as_instances` sowie die Funktionen `create_formatter` und `print_table` aus dem `structly`-Paket zu importieren. Wenn die Imports erfolgreich sind, wird das Programm die Nachricht "Successfully imported all required symbols!" ausgeben. Speichern Sie die Datei und verlassen Sie den Editor. Jetzt führen wir diesen Test aus:

```bash
cd ~/project
python test_structly.py
```

Der Befehl `cd ~/project` wechselt das aktuelle Arbeitsverzeichnis in das Projektverzeichnis. Der Befehl `python test_structly.py` führt das Skript `test_structly.py` aus. Wenn alles korrekt funktioniert, sollten Sie die Nachricht "Successfully imported all required symbols!" auf dem Bildschirm sehen.
