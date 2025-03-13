# Verwendung dynamischer Importe

In der Programmierung werden Importe verwendet, um Code aus anderen Modulen einzubinden, damit wir deren Funktionalität nutzen können. Manchmal kann es jedoch dazu führen, dass der Code etwas unübersichtlich und schwer zu verstehen wird, wenn Importe mitten in einer Datei stehen. In diesem Abschnitt lernen wir, wie wir dynamische Importe verwenden können, um dieses Problem zu lösen. Dynamische Importe sind eine leistungsstarke Funktion, die es uns ermöglicht, Module zur Laufzeit zu laden. Das bedeutet, dass wir ein Modul erst laden, wenn wir es tatsächlich benötigen.

Zunächst müssen wir die Importanweisungen entfernen, die derzeit nach der `TableFormatter`-Klasse platziert sind. Diese Importe sind statische Importe, die beim Start des Programms geladen werden. Öffnen Sie dazu die Datei `tableformat/formatter.py` in der WebIDE. Sobald Sie die Datei geöffnet haben, suchen Sie die folgenden Zeilen und löschen Sie sie:

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Wenn Sie jetzt versuchen, das Programm auszuführen, indem Sie den folgenden Befehl im Terminal ausführen:

```bash
python3 stock.py
```

wird das Programm fehlschlagen. Der Grund dafür ist, dass die Formatierer nicht im `_formats`-Dictionary registriert werden. Sie werden eine Fehlermeldung über ein unbekanntes Format sehen. Dies liegt daran, dass das Programm die Formatierer-Klassen nicht finden kann, die es benötigt, um richtig zu funktionieren.

Um dieses Problem zu beheben, ändern weir die `create_formatter`-Funktion. Das Ziel ist es, das erforderliche Modul dynamisch zu importieren, wenn es benötigt wird. Aktualisieren Sie die Funktion wie unten gezeigt:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

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

Die wichtigste Zeile in dieser Funktion ist:

```python
__import__(f'{__package__}.formats.{name}')
```

Diese Zeile importiert das Modul dynamisch basierend auf dem Formatnamen. Wenn das Modul importiert wird, registriert sich seine Subklasse von `TableFormatter` automatisch. Dies ist dank der `__init_subclass__`-Methode möglich, die wir zuvor hinzugefügt haben. Diese Methode ist eine spezielle Python-Methode, die aufgerufen wird, wenn eine Subklasse erstellt wird. In unserem Fall wird sie verwendet, um die Formatierer-Klasse zu registrieren.

Nachdem Sie diese Änderungen vorgenommen haben, speichern Sie die Datei. Führen Sie dann das Programm erneut aus, indem Sie den folgenden Befehl verwenden:

```bash
python3 stock.py
```

Das Programm sollte jetzt korrekt funktionieren, obwohl wir die statischen Importe entfernt haben. Um zu überprüfen, ob der dynamische Import wie erwartet funktioniert, leeren wir das `_formats`-Dictionary und rufen dann die `create_formatter`-Funktion auf. Führen Sie den folgenden Befehl im Terminal aus:

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

Diese Ausgabe bestätigt, dass der dynamische Import das Modul lädt und die Formatierer-Klasse bei Bedarf registriert.

Durch die Verwendung dynamischer Importe und der Klassenregistrierung haben wir eine sauberere und wartbarere Code-Struktur erstellt. Hier sind die Vorteile:

1. Alle Importe befinden sich jetzt am Anfang der Datei, was den Python-Konventionen entspricht. Dies macht den Code leichter zu lesen und zu verstehen.
2. Wir haben zirkuläre Importe eliminiert. Zirkuläre Importe können in einem Programm Probleme verursachen, wie z. B. unendliche Schleifen oder schwer zu debuggende Fehler.
3. Der Code ist flexibler. Jetzt können wir neue Formatierer hinzufügen, ohne die `create_formatter`-Funktion zu ändern. Dies ist in einer realen Anwendung sehr nützlich, in der möglicherweise im Laufe der Zeit neue Funktionen hinzugefügt werden.

Dieses Muster der Verwendung dynamischer Importe und Klassenregistrierung wird häufig in Plug-In-Systemen und Frameworks eingesetzt. In diesen Systemen müssen Komponenten dynamisch auf der Grundlage der Benutzeranforderungen oder der Programmvoraussetzungen geladen werden.
