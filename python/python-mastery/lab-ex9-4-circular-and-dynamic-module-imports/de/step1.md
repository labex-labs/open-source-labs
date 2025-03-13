# Das Import-Problem verstehen

Beginnen wir damit, zu verstehen, was Modulimporte sind. In Python verwenden Sie die `import`-Anweisung, wenn Sie Funktionen, Klassen oder Variablen aus einer anderen Datei (Modul) verwenden möchten. Allerdings kann die Art und Weise, wie Sie Ihre Importe strukturieren, zu verschiedenen Problemen führen.

Nun werden wir uns ein Beispiel für eine problematische Modulstruktur ansehen. Der Code in `tableformat/formatter.py` enthält Importe, die über die gesamte Datei verteilt sind. Dies mag zunächst nicht wie ein großes Problem erscheinen, aber es führt zu Wartungs- und Abhängigkeitsproblemen.

Öffnen Sie zunächst den Dateiexplorer der WebIDE und navigieren Sie zum Verzeichnis `structly`. Wir werden ein paar Befehle ausführen, um die aktuelle Struktur des Projekts zu verstehen. Der `cd`-Befehl wird verwendet, um das aktuelle Arbeitsverzeichnis zu ändern, und der `ls -la`-Befehl listet alle Dateien und Verzeichnisse im aktuellen Verzeichnis auf, einschließlich versteckter Dateien.

```bash
cd ~/project/structly
ls -la
```

Dadurch werden Ihnen die Dateien im Projektverzeichnis angezeigt. Jetzt werden wir uns eine der problematischen Dateien mit dem `cat`-Befehl ansehen, der den Inhalt einer Datei anzeigt.

```bash
cat tableformat/formatter.py
```

Sie sollten Code ähnlich dem folgenden sehen:

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Beachten Sie die Platzierung der Importanweisungen in der Mitte der Datei. Dies ist aus mehreren Gründen problematisch:

1. Es macht den Code schwieriger zu lesen und zu warten. Wenn Sie sich eine Datei ansehen, erwarten Sie, alle Importe am Anfang zu sehen, damit Sie schnell verstehen können, von welchen externen Modulen die Datei abhängt.
2. Es kann zu zirkulären Importproblemen führen. Zirkuläre Importe treten auf, wenn zwei oder mehr Module voneinander abhängen, was Fehler verursachen und dazu führen kann, dass Ihr Code unerwartet verhält.
3. Es bricht die Python-Konvention, alle Importe am Anfang einer Datei zu platzieren. Die Einhaltung von Konventionen macht Ihren Code lesbarer und leichter für andere Entwickler zu verstehen.

In den folgenden Schritten werden wir diese Probleme ausführlicher untersuchen und lernen, wie wir sie beheben können.
