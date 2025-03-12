# Implementierung von Mixin-Klassen für die Formatierung

In diesem Schritt werden wir uns mit Mixin-Klassen (Mixin-Klassen sind in der Informatik eine spezielle Art von Klasse) befassen. Mixin-Klassen sind eine sehr nützliche Technik in Python. Sie ermöglichen es Ihnen, Klassen zusätzliche Funktionalität hinzuzufügen, ohne ihren ursprünglichen Code zu ändern. Dies ist großartig, da es hilft, Ihren Code modular und leicht zu verwalten zu halten.

## Was sind Mixin-Klassen?

Eine Mixin-Klasse ist eine spezielle Art von Klasse. Ihr Hauptzweck besteht darin, einige Funktionen bereitzustellen, die von einer anderen Klasse geerbt werden können. Eine Mixin-Klasse ist jedoch nicht dafür gedacht, allein verwendet zu werden. Sie erstellen keine Instanz einer Mixin-Klasse direkt. Stattdessen verwenden Sie sie, um bestimmte Funktionen auf kontrollierte und vorhersehbare Weise anderen Klassen hinzuzufügen. Dies ist eine Form der Mehrfachvererbung, bei der eine Klasse von mehr als einer Basisklasse erben kann.

Jetzt implementieren wir zwei Mixin-Klassen in unserer Datei `tableformat.py`. Öffnen Sie zunächst die Datei im Editor. Sie können dies tun, indem Sie die folgenden Befehle in Ihrem Terminal ausführen:

```bash
cd ~/project
code tableformat.py
```

Sobald die Datei geöffnet ist, fügen Sie die folgenden Klassendefinitionen am Ende der Datei, aber vor allen bestehenden Funktionen, hinzu.

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

Diese `ColumnFormatMixin`-Klasse bietet die Funktionalität zur Spaltenformatierung. Die Klassenvariable `formats` ist eine Liste, die Formatcodes enthält. Diese Codes werden verwendet, um die Daten in jeder Spalte zu formatieren. Die Methode `row()` nimmt die Zeilendaten entgegen, wendet die Formatcodes auf jedes Element in der Zeile an und übergibt dann die formatierten Zeilendaten an die Basisklasse mit `super().row(rowdata)`.

Fügen Sie als Nächstes eine andere Mixin-Klasse hinzu, die dafür sorgt, dass die Tabellenüberschriften in Großbuchstaben angezeigt werden:

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

Diese `UpperHeadersMixin`-Klasse wandelt den Text der Überschriften in Großbuchstaben um. Sie nimmt die Liste der Überschriften entgegen, wandelt jede Überschrift in Großbuchstaben um und übergibt dann die geänderten Überschriften an die `headings()`-Methode der Basisklasse mit `super().headings()`.

## Verwendung der Mixin-Klassen

Testen wir unsere neuen Mixin-Klassen. Wir werden etwas Python-Code ausführen, um zu sehen, wie sie funktionieren.

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Wenn Sie diesen Code ausführen, sollten Sie eine schön formatierte Ausgabe sehen. Die Preisspalte wird aufgrund der Formatierung, die von der `ColumnFormatMixin`-Klasse bereitgestellt wird, konsistente Dezimalstellen haben.

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Jetzt probieren wir die `UpperHeadersMixin`-Klasse aus. Führen Sie den folgenden Code aus:

```python
python3 -c "
from tableformat import TextTableFormatter, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Dieser Code sollte die Überschriften in Großbuchstaben anzeigen.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

## Verständnis der kooperativen Vererbung

Beachten Sie, dass wir in unseren Mixin-Klassen `super().method()` verwenden. Dies wird "kooperative Vererbung" genannt. Bei der kooperativen Vererbung arbeiten alle Klassen in der Vererbungskette zusammen. Wenn eine Klasse `super().method()` aufruft, bittet sie die nächste Klasse in der Kette, ihren Teil der Aufgabe auszuführen. Auf diese Weise können die Klassen in der Kette jeweils ihr eigenes Verhalten zum gesamten Prozess hinzufügen.

Die Reihenfolge der Vererbung ist sehr wichtig. Wenn wir `class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter)` definieren, sucht Python zunächst in `ColumnFormatMixin` nach Methoden und dann in `TextTableFormatter`. Wenn also `super().row()` in der `ColumnFormatMixin` aufgerufen wird, bezieht sich dies auf `TextTableFormatter.row()`.

Wir können sogar beide Mixins kombinieren. Führen Sie den folgenden Code aus:

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Dieser Code wird uns sowohl Großbuchstabenüberschriften als auch formatierte Zahlen liefern.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Im nächsten Schritt werden wir diese Mixins einfacher zu verwenden machen, indem wir die Funktion `create_formatter()` verbessern.
