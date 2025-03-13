# Implementierung der Subklassen-Registrierung

In der Programmierung können zirkuläre Importe ein kniffliges Problem darstellen. Anstatt die Formatierer-Klassen direkt zu importieren, können wir ein Registrierungsmuster verwenden. In diesem Muster registrieren sich die Subklassen bei ihrer Basisklasse. Dies ist eine gängige und effektive Methode, um zirkuläre Importe zu vermeiden.

Zunächst verstehen wir, wie wir den Modulnamen einer Klasse herausfinden können. Der Modulname ist wichtig, da wir ihn in unserem Registrierungsmuster verwenden werden. Dazu führen wir einen Python-Befehl im Terminal aus.

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

Wenn Sie diesen Befehl ausführen, sehen Sie eine Ausgabe wie diese:

```
structly.tableformat.formats.text
text
```

Diese Ausgabe zeigt, dass wir den Namen des Moduls direkt aus der Klasse extrahieren können. Wir werden diesen Modulnamen später verwenden, um die Subklassen zu registrieren.

Jetzt ändern wir die `TableFormatter`-Klasse in der Datei `tableformat/formatter.py`, um einen Registrierungsmechanismus hinzuzufügen. Öffnen Sie diese Datei in der WebIDE. Wir fügen der `TableFormatter`-Klasse etwas Code hinzu. Dieser Code wird uns helfen, die Subklassen automatisch zu registrieren.

```python
class TableFormatter(ABC):
    _formats = { }  # Dictionary to store registered formatters

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

Die Methode `__init_subclass__` ist eine spezielle Methode in Python. Sie wird aufgerufen, wenn immer eine Subklasse von `TableFormatter` erstellt wird. In dieser Methode extrahieren wir den Modulnamen der Subklasse und verwenden ihn als Schlüssel, um die Subklasse im `_formats`-Dictionary zu registrieren.

Als Nächstes müssen wir die Funktion `create_formatter` ändern, um das Registrierungs-Dictionary zu verwenden. Diese Funktion ist dafür verantwortlich, den passenden Formatierer basierend auf dem gegebenen Namen zu erstellen.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Nachdem Sie diese Änderungen vorgenommen haben, speichern Sie die Datei. Dann testen wir, ob das Programm noch funktioniert. Wir führen das Skript `stock.py` aus.

```bash
python3 stock.py
```

Wenn das Programm korrekt läuft, bedeutet dies, dass unsere Änderungen nichts kaputt gemacht haben. Jetzt schauen wir uns den Inhalt des `_formats`-Dictionarys an, um zu sehen, wie die Registrierung funktioniert.

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

Sie sollten eine Ausgabe wie diese sehen:

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

Diese Ausgabe bestätigt, dass unsere Subklassen korrekt im `_formats`-Dictionary registriert werden. Allerdings haben wir immer noch einige Importe in der Mitte der Datei. Im nächsten Schritt werden wir dieses Problem mithilfe von dynamischen Importen beheben.
