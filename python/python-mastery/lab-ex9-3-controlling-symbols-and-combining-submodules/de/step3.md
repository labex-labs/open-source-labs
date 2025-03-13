# Exportieren aller Symbole aus dem Paket

In Python ist die Organisation von Paketen von entscheidender Bedeutung für die effektive Verwaltung von Code. Jetzt werden wir die Organisation unseres Pakets einen Schritt weiter treiben. Wir werden festlegen, welche Symbole auf Paketebene exportiert werden sollen. Das Exportieren von Symbolen bedeutet, bestimmte Funktionen, Klassen oder Variablen für andere Teile Ihres Codes oder für andere Entwickler, die Ihr Paket verwenden könnten, verfügbar zu machen.

## Hinzufügen von `__all__` zum Paket

Wenn Sie mit Python-Paketen arbeiten, möchten Sie möglicherweise steuern, welche Symbole zugänglich sind, wenn jemand die Anweisung `from structly import *` verwendet. Hier kommt die Liste `__all__` zum Einsatz. Indem Sie eine `__all__`-Liste zur `__init__.py`-Datei des Pakets hinzufügen, können Sie genau steuern, welche Symbole verfügbar sind, wenn jemand die Anweisung `from structly import *` verwendet.

Zunächst erstellen oder aktualisieren wir die `__init__.py`-Datei. Wir verwenden den Befehl `touch`, um die Datei zu erstellen, falls sie noch nicht existiert.

```bash
touch ~/project/structly/__init__.py
```

Öffnen Sie nun die `__init__.py`-Datei und fügen Sie eine `__all__`-Liste hinzu. Diese Liste sollte alle Symbole enthalten, die wir exportieren möchten. Die Symbole sind gruppiert nach ihrer Herkunft, z. B. aus den Modulen `structure`, `reader` und `tableformat`.

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

# Define what symbols are exported when using "from structly import *"
__all__ = ['Structure',  # from structure
           'read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns',  # from reader
           'create_formatter', 'print_table']  # from tableformat
```

Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei und verlassen Sie den Editor.

## Verständnis von `import *`

Das Muster `from module import *` wird in den meisten Python-Codes im Allgemeinen nicht empfohlen. Es gibt mehrere Gründe dafür:

1. Es kann Ihren Namensraum mit unerwarteten Symbolen verschmutzen. Dies bedeutet, dass Sie möglicherweise Variablen oder Funktionen in Ihrem aktuellen Namensraum haben, die Sie nicht erwartet haben, was zu Namenskonflikten führen kann.
2. Es ist unklar, woher bestimmte Symbole stammen. Wenn Sie `import *` verwenden, ist es schwierig zu sagen, aus welchem Modul ein Symbol stammt, was Ihren Code schwerer zu verstehen und zu warten macht.
3. Es kann zu Shadowing-Problemen führen. Shadowing tritt auf, wenn eine lokale Variable oder Funktion denselben Namen wie eine Variable oder Funktion aus einem anderen Modul hat, was zu unerwartetem Verhalten führen kann.

Es gibt jedoch bestimmte Fälle, in denen die Verwendung von `import *` angemessen ist:

- Für Pakete, die als ein zusammenhängendes Ganzes verwendet werden sollen. Wenn ein Paket als eine Einheit verwendet werden soll, kann die Verwendung von `import *` den Zugang zu allen erforderlichen Symbolen erleichtern.
- Wenn ein Paket über `__all__` eine klare Schnittstelle definiert. Durch die Verwendung der `__all__`-Liste können Sie steuern, welche Symbole exportiert werden, was die Verwendung von `import *` sicherer macht.
- Für die interaktive Verwendung, z. B. in einer Python-REPL (Read-Eval-Print Loop). In einer interaktiven Umgebung kann es praktisch sein, alle Symbole auf einmal zu importieren.

## Testen mit Import \*

Um zu überprüfen, dass wir alle Symbole auf einmal importieren können, erstellen wir eine weitere Testdatei. Wir verwenden den Befehl `touch`, um die Datei zu erstellen.

```bash
touch ~/project/test_import_all.py
```

Öffnen Sie nun die `test_import_all.py`-Datei und fügen Sie den folgenden Inhalt hinzu. Dieser Code importiert alle Symbole aus dem `structly`-Paket und testet dann, ob einige der wichtigen Symbole verfügbar sind.

```python
# Test importing everything at once

from structly import *

# Try using the imported symbols
print(f"Structure symbol is available: {Structure is not None}")
print(f"read_csv_as_instances symbol is available: {read_csv_as_instances is not None}")
print(f"create_formatter symbol is available: {create_formatter is not None}")
print(f"print_table symbol is available: {print_table is not None}")

print("All symbols successfully imported!")
```

Speichern Sie die Datei und verlassen Sie den Editor. Jetzt führen wir den Test aus. Navigieren Sie zunächst mit dem Befehl `cd` in das Projektverzeichnis und führen Sie dann das Python-Skript aus.

```bash
cd ~/project
python test_import_all.py
```

Wenn alles korrekt eingerichtet ist, sollten Sie eine Bestätigung sehen, dass alle Symbole erfolgreich importiert wurden.
