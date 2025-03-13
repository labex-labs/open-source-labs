# Modulsplitting für eine bessere Codeorganisation

Wenn Ihre Python-Projekte wachsen, können Sie feststellen, dass eine einzelne Moduldatei ziemlich groß wird und mehrere verwandte, aber unterschiedliche Komponenten enthält. In einem solchen Fall ist es eine gute Praxis, das Modul in ein Paket mit Untermodulen aufzuteilen. Dieser Ansatz macht Ihren Code besser organisiert, leichter zu warten und skalierbarer.

## Verständnis der aktuellen Struktur

Das Modul `tableformat.py` ist ein gutes Beispiel für ein großes Modul. Es enthält mehrere Formatiererklassen, die jeweils für die Formatierung von Daten auf unterschiedliche Weise verantwortlich sind:

- `TableFormatter` (Basis-Klasse): Dies ist die Basisklasse für alle anderen Formatiererklassen. Sie definiert die grundlegende Struktur und Methoden, die die anderen Klassen erben und implementieren werden.
- `TextTableFormatter`: Diese Klasse formatiert Daten im Klartextformat.
- `CSVTableFormatter`: Diese Klasse formatiert Daten im CSV-Format (Comma-Separated Values, engl. für "durch Kommas getrennte Werte").
- `HTMLTableFormatter`: Diese Klasse formatiert Daten im HTML-Format (Hypertext Markup Language, engl. für "Hypertext-Auszeichnungssprache").

Wir werden dieses Modul in eine Paketstruktur umorganisieren, wobei für jeden Formatierertyp separate Dateien erstellt werden. Dies macht den Code modularer und leichter zu verwalten.

## Schritt 1: Bereinigen von Cache-Dateien

Bevor wir mit der Umorganisation des Codes beginnen, ist es eine gute Idee, alle Python-Cache-Dateien zu bereinigen. Diese Dateien werden von Python erstellt, um die Ausführung Ihres Codes zu beschleunigen, können aber manchmal Probleme verursachen, wenn Sie Änderungen an Ihrem Code vornehmen.

```bash
cd ~/project/structly
rm -rf __pycache__
```

In den obigen Befehlen wechselt `cd ~/project/structly` das aktuelle Verzeichnis in das `structly`-Verzeichnis Ihres Projekts. `rm -rf __pycache__` löscht das `__pycache__`-Verzeichnis und all seinen Inhalt. Die Option `-r` steht für rekursiv, was bedeutet, dass alle Dateien und Unterverzeichnisse innerhalb des `__pycache__`-Verzeichnisses gelöscht werden. Die Option `-f` steht für force (englisch für "zwingen"), was bedeutet, dass die Dateien ohne Bestätigungsmeldung gelöscht werden.

## Schritt 2: Erstellen der neuen Paketstruktur

Jetzt erstellen wir eine neue Verzeichnisstruktur für unser Paket. Wir werden ein Verzeichnis namens `tableformat` und ein Unterverzeichnis namens `formats` darin erstellen.

```bash
mkdir -p tableformat/formats
```

Der Befehl `mkdir` wird verwendet, um Verzeichnisse zu erstellen. Die Option `-p` steht für parents (englisch für "Eltern"), was bedeutet, dass alle erforderlichen übergeordneten Verzeichnisse erstellt werden, falls sie nicht existieren. Wenn also das `tableformat`-Verzeichnis nicht existiert, wird es zuerst erstellt, und dann wird das `formats`-Verzeichnis darin erstellt.

## Schritt 3: Verschieben und Umbenennen der ursprünglichen Datei

Als Nächstes verschieben wir die ursprüngliche `tableformat.py`-Datei in die neue Struktur und benennen sie in `formatter.py` um.

```bash
mv tableformat.py tableformat/formatter.py
```

Der Befehl `mv` wird verwendet, um Dateien zu verschieben oder umzubenennen. In diesem Fall verschieben wir die `tableformat.py`-Datei in das `tableformat`-Verzeichnis und benennen sie in `formatter.py` um.

## Schritt 4: Aufteilen des Codes in separate Dateien

Jetzt müssen wir Dateien für jeden Formatierer erstellen und den relevanten Code in sie verschieben.

### 1. Erstellen der Basis-Formatiererdatei

```bash
touch tableformat/formatter.py
```

Der Befehl `touch` wird verwendet, um eine leere Datei zu erstellen. In diesem Fall erstellen wir eine Datei namens `formatter.py` im `tableformat`-Verzeichnis.

Wir werden die Basisklasse `TableFormatter` und alle allgemeinen Hilfsfunktionen wie `print_table` und `create_formatter` in dieser Datei belassen. Die Datei sollte in etwa so aussehen:

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

Die Variable `__all__` wird verwendet, um anzugeben, welche Symbole importiert werden sollen, wenn Sie `from module import *` verwenden. In diesem Fall geben wir an, dass nur die Symbole `TableFormatter`, `print_table` und `create_formatter` importiert werden sollen.

Die Klasse `TableFormatter` ist die Basisklasse für alle anderen Formatiererklassen. Sie definiert zwei Methoden, `headings` und `row`, die von den Unterklassen implementiert werden sollen.

Die Funktion `print_table` ist eine Hilfsfunktion, die eine Liste von Objekten, eine Liste von Spaltennamen und ein Formatiererobjekt nimmt und die Daten in einer formatierten Tabelle ausgibt.

Die Funktion `create_formatter` ist eine Fabrikfunktion, die einen Formatnamen als Argument nimmt und ein geeignetes Formatiererobjekt zurückgibt.

Speichern Sie die Datei und verlassen Sie den Editor, nachdem Sie diese Änderungen vorgenommen haben.

### 2. Erstellen des Text-Formatierers

```bash
touch tableformat/formats/text.py
```

Wir werden nur die Klasse `TextTableFormatter` in diese Datei hinzufügen.

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

Die Variable `__all__` gibt an, dass nur das Symbol `TextTableFormatter` importiert werden soll, wenn Sie `from module import *` verwenden.

Die Anweisung `from ..formatter import TableFormatter` importiert die Klasse `TableFormatter` aus der Datei `formatter.py` im übergeordneten Verzeichnis.

Die Klasse `TextTableFormatter` erbt von der Klasse `TableFormatter` und implementiert die Methoden `headings` und `row`, um die Daten im Klartextformat zu formatieren.

Speichern Sie die Datei und verlassen Sie den Editor, nachdem Sie diese Änderungen vorgenommen haben.

### 3. Erstellen des CSV-Formatierers

```bash
touch tableformat/formats/csv.py
```

Wir werden nur die Klasse `CSVTableFormatter` in diese Datei hinzufügen.

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

Ähnlich wie in den vorherigen Schritten geben wir die Variable `__all__` an, importieren die Klasse `TableFormatter` und implementieren die Methoden `headings` und `row`, um die Daten im CSV-Format zu formatieren.

Speichern Sie die Datei und verlassen Sie den Editor, nachdem Sie diese Änderungen vorgenommen haben.

### 4. Erstellen des HTML-Formatierers

```bash
touch tableformat/formats/html.py
```

Wir werden nur die Klasse `HTMLTableFormatter` in diese Datei hinzufügen.

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

Wir geben erneut die Variable `__all__` an, importieren die Klasse `TableFormatter` und implementieren die Methoden `headings` und `row`, um die Daten im HTML-Format zu formatieren.

Speichern Sie die Datei und verlassen Sie den Editor, nachdem Sie diese Änderungen vorgenommen haben.

## Schritt 5: Erstellen von Paket-Initialisierungsdateien

In Python werden `__init__.py`-Dateien verwendet, um Verzeichnisse als Python-Pakete zu markieren. Wir müssen `__init__.py`-Dateien sowohl im `tableformat`- als auch im `formats`-Verzeichnis erstellen.

### 1. Erstellen einer für das `tableformat`-Paket

```bash
touch tableformat/__init__.py
```

Fügen Sie den folgenden Inhalt in die Datei ein:

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

Diese Anweisung importiert alle Symbole aus der Datei `formatter.py` und macht sie verfügbar, wenn Sie das `tableformat`-Paket importieren.

Speichern Sie die Datei und verlassen Sie den Editor, nachdem Sie diese Änderungen vorgenommen haben.

### 2. Erstellen einer für das `formats`-Paket

```bash
touch tableformat/formats/__init__.py
```

Sie können diese Datei leer lassen oder einen einfachen Docstring hinzufügen:

```python
'''
Format implementations for different output formats.
'''
```

Der Docstring gibt eine kurze Beschreibung darüber, was das `formats`-Paket macht.

Speichern Sie die Datei und verlassen Sie den Editor, nachdem Sie diese Änderungen vorgenommen haben.

## Schritt 6: Testen der neuen Struktur

Erstellen wir einen einfachen Test, um zu überprüfen, ob unsere Änderungen korrekt funktionieren.

```bash
cd ~/project
touch test_tableformat.py
```

Fügen Sie den folgenden Inhalt in die Datei `test_tableformat.py` ein:

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

Dieser Testcode importiert die erforderlichen Funktionen und Klassen aus dem `structly`-Paket, erstellt Formatierer jeder Art, definiert einige Testdaten und testet dann jeden Formatierer, indem er die Daten im entsprechenden Format ausgibt.

Speichern Sie die Datei und verlassen Sie den Editor, nachdem Sie diese Änderungen vorgenommen haben. Jetzt führen Sie den Test aus:

```bash
python test_tableformat.py
```

Sie sollten die gleichen Daten in drei verschiedenen Formaten (Text, CSV und HTML) formatiert sehen. Wenn Sie die erwartete Ausgabe sehen, bedeutet dies, dass Ihre Codeumorganisation erfolgreich war.
