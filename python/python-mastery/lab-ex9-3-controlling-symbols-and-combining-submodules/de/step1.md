# Verständnis der Komplexität von Paket-Imports

Wenn Sie mit Python-Paketen beginnen, werden Sie schnell feststellen, dass das Importieren von Modulen recht kompliziert und umständlich werden kann. Diese Komplexität kann es schwieriger machen, Ihren Code zu lesen und zu schreiben. In diesem Lab werden wir uns dieser Frage genauer ansehen und lernen, wie wir den Importprozess vereinfachen können.

## Aktuelle Importstruktur

Zunächst öffnen wir das Terminal. Das Terminal ist ein leistungsfähiges Werkzeug, das es Ihnen ermöglicht, mit dem Betriebssystem Ihres Computers zu interagieren. Sobald das Terminal geöffnet ist, müssen wir in das Projektverzeichnis wechseln. Das Projektverzeichnis ist der Ort, an dem alle Dateien unseres Python-Projekts gespeichert sind. Dazu verwenden wir den Befehl `cd`, der für "change directory" (Verzeichnis wechseln) steht.

```bash
cd ~/project
```

Jetzt, da wir uns im Projektverzeichnis befinden, lassen Sie uns die aktuelle Struktur des `structly`-Pakets untersuchen. Ein Paket in Python ist eine Möglichkeit, verwandte Module zu organisieren. Wir können den Befehl `ls -la` verwenden, um alle Dateien und Verzeichnisse innerhalb des `structly`-Pakets aufzulisten, einschließlich versteckter Dateien.

```bash
ls -la structly
```

Sie werden feststellen, dass es mehrere Python-Module innerhalb des `structly`-Pakets gibt. Diese Module enthalten Funktionen und Klassen, die wir in unserem Code verwenden können. Wenn wir jedoch die Funktionalität dieser Module nutzen möchten, müssen wir derzeit lange Importanweisungen verwenden. Beispielsweise:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

Diese langen Importpfade können mühsam zu schreiben sein, insbesondere wenn Sie sie mehrmals in Ihrem Code verwenden müssen. Sie machen Ihren Code auch weniger lesbar, was ein Problem sein kann, wenn Sie versuchen, Ihren Code zu verstehen oder zu debuggen. In diesem Lab werden wir lernen, wie wir das Paket so organisieren können, dass diese Imports einfacher werden.

Lassen Sie uns zunächst den Inhalt der `__init__.py`-Datei des Pakets betrachten. Die `__init__.py`-Datei ist eine besondere Datei in Python-Paketen. Sie wird ausgeführt, wenn das Paket importiert wird, und kann verwendet werden, um das Paket zu initialisieren und alle erforderlichen Imports einzurichten.

```bash
cat structly/__init__.py
```

Sie werden wahrscheinlich feststellen, dass die `__init__.py`-Datei entweder leer ist oder nur sehr wenig Code enthält. In den nächsten Schritten werden wir diese Datei ändern, um unsere Importanweisungen zu vereinfachen.

## Das Ziel

Bis zum Ende dieses Labs möchten wir in der Lage sein, viel einfachere Importanweisungen zu verwenden. Anstelle der langen Importpfade, die wir zuvor gesehen haben, können wir Anweisungen wie diese verwenden:

```python
from structly import Structure, read_csv_as_instances, create_formatter, print_table
```

Oder sogar:

```python
from structly import *
```

Die Verwendung dieser einfacheren Importanweisungen wird unseren Code sauberer und einfacher zu bearbeiten machen. Es wird uns auch Zeit und Mühe sparen, wenn wir unseren Code schreiben und warten.
