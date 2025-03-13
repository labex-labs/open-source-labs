# Erstellen der Paketstruktur

Jetzt werden wir unser Python-Paket erstellen. Aber zuerst verstehen wir, was ein Python-Paket ist. Ein Python-Paket ist eine Möglichkeit, verwandte Python-Module in einer einzigen Verzeichnis-Hierarchie zu organisieren. Es hilft, Code effektiver zu verwalten und wiederzuverwenden. Um ein Python-Paket zu erstellen, müssen wir die folgenden Schritte befolgen:

1. Erstellen Sie ein Verzeichnis mit dem Paketnamen. Dieses Verzeichnis dient als Container für alle Module, die zum Paket gehören.
2. Erstellen Sie eine `__init__.py`-Datei innerhalb dieses Verzeichnisses. Diese Datei ist wichtig, da sie Python dazu bringt, das Verzeichnis als Paket zu erkennen. Wenn Sie das Paket importieren, wird der Code in `__init__.py` ausgeführt, der verwendet werden kann, um das Paket zu initialisieren.
3. Verschieben Sie unsere Python-Moduldateien in dieses Verzeichnis. Dieser Schritt stellt sicher, dass all der verwandte Code innerhalb des Pakets zusammengefasst wird.

Lassen Sie uns die Paketstruktur Schritt für Schritt erstellen:

1. Zuerst erstellen Sie ein Verzeichnis namens `structly`. Dies wird das Root-Verzeichnis unseres Pakets sein.

```bash
mkdir structly
```

2. Erstellen Sie als Nächstes eine leere `__init__.py`-Datei innerhalb des `structly`-Verzeichnisses.

```bash
touch structly/__init__.py
```

Die `__init__.py`-Datei kann leer sein, aber sie ist erforderlich, damit Python das Verzeichnis als Paket behandelt. Wenn Sie das Paket importieren, wird der Code in `__init__.py` ausgeführt, der verwendet werden kann, um das Paket zu initialisieren.

3. Jetzt verschieben wir unsere Python-Moduldateien in das `structly`-Verzeichnis. Diese Moduldateien enthalten die Funktionen und Klassen, die wir in unser Paket aufnehmen möchten.

```bash
mv structure.py validate.py reader.py tableformat.py structly/
```

4. Überprüfen Sie, ob alle Dateien korrekt verschoben wurden. Wir können den Befehl `ls -l` verwenden, um den Inhalt des `structly`-Verzeichnisses aufzulisten.

```bash
ls -l structly/
```

Sie sollten die folgenden Dateien aufgelistet sehen:

```
__init__.py
reader.py
structure.py
tableformat.py
validate.py
```

Jetzt haben wir eine grundlegende Paketstruktur erstellt. Die Verzeichnis-Hierarchie sollte wie folgt aussehen:

```
project/
├── portfolio.csv
├── stock.py
└── structly/
    ├── __init__.py
    ├── reader.py
    ├── structure.py
    ├── tableformat.py
    └── validate.py
```

Im nächsten Schritt werden wir die Import-Anweisungen korrigieren, damit das Paket richtig funktioniert.
