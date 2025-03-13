# Untersuchung von zirkulären Importen

Ein zirkulärer Import tritt auf, wenn zwei oder mehr Module voneinander abhängen. Genauer gesagt, wenn Modul A Modul B importiert und Modul B ebenfalls Modul A importiert, entweder direkt oder indirekt. Dies schafft eine Abhängigkeits-Schleife, die das Import-System von Python nicht richtig auflösen kann. Einfacher ausgedrückt: Python gerät in eine Schleife, in der es versucht, herauszufinden, welches Modul zuerst importiert werden soll, und dies kann zu Fehlern in Ihrem Programm führen.

Lassen Sie uns mit unserem Code experimentieren, um zu sehen, wie zirkuläre Importe Probleme verursachen können.

Zunächst werden wir das Aktienprogramm ausführen, um zu prüfen, ob es mit der aktuellen Struktur funktioniert. Dieser Schritt hilft uns, eine Basislinie zu erstellen und das Programm in der erwarteten Weise laufen zu sehen, bevor wir irgendwelche Änderungen vornehmen.

```bash
cd ~/project/structly
python3 stock.py
```

Das Programm sollte korrekt laufen und die Aktiendaten in einer formatierten Tabelle anzeigen. Wenn dies der Fall ist, bedeutet dies, dass die aktuelle Code-Struktur ohne zirkuläre Importprobleme funktioniert.

Jetzt werden wir die Datei `formatter.py` ändern. Normalerweise ist es eine gute Praxis, Importe an den Anfang einer Datei zu verschieben. Dies macht den Code besser organisiert und leichter auf einen Blick zu verstehen.

```bash
cd ~/project/structly
```

Öffnen Sie `tableformat/formatter.py` in der WebIDE. Wir werden die folgenden Importe an den Anfang der Datei verschieben, direkt nach den vorhandenen Importen. Diese Importe sind für verschiedene Tabellenformatierer, wie Text, CSV und HTML.

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Der Anfang der Datei sollte jetzt wie folgt aussehen:

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

Speichern Sie die Datei und versuchen Sie, das Aktienprogramm erneut auszuführen.

```bash
python3 stock.py
```

Sie sollten eine Fehlermeldung darüber sehen, dass `TableFormatter` nicht definiert ist. Dies ist ein eindeutiges Zeichen für ein zirkuläres Importproblem.

Das Problem tritt auf, weil die folgenden Ereignisse nacheinander eintreten:

1. `formatter.py` versucht, `TextTableFormatter` aus `formats/text.py` zu importieren.
2. `formats/text.py` importiert `TableFormatter` aus `formatter.py`.
3. Wenn Python versucht, diese Importe aufzulösen, gerät es in eine Schleife, weil es nicht entscheiden kann, welches Modul zuerst vollständig importiert werden soll.

Lassen Sie uns unsere Änderungen rückgängig machen, damit das Programm wieder funktioniert. Bearbeiten Sie `tableformat/formatter.py` und verschieben Sie die Importe zurück an ihre ursprüngliche Stelle (nach der Definition der `TableFormatter`-Klasse).

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
```

Führen Sie das Programm erneut aus, um zu bestätigen, dass es funktioniert.

```bash
python3 stock.py
```

Dies zeigt, dass obwohl es in Bezug auf die Code-Organisation nicht die beste Praxis ist, Importe in der Mitte der Datei zu haben, dies getan wurde, um ein zirkuläres Importproblem zu vermeiden. In den nächsten Schritten werden wir bessere Lösungen untersuchen.
