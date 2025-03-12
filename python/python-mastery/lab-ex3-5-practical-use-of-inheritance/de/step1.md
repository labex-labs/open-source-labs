# Das Problem verstehen

In diesem Lab werden wir uns mit Vererbung (inheritance) in Python befassen und lernen, wie sie uns dabei helfen kann, Code zu schreiben, der sowohl erweiterbar als auch anpassungsfähig ist. Vererbung ist ein mächtiges Konzept in der objektorientierten Programmierung, bei dem eine Klasse Attribute und Methoden von einer anderen Klasse erben kann. Dies ermöglicht es uns, Code wiederzuverwenden und auf bestehendem Code komplexere Funktionen aufzubauen.

Beginnen wir damit, uns die vorhandene Funktion `print_table()` anzusehen. Diese Funktion werden wir verbessern, um sie in Bezug auf die Ausgabeformate flexibler zu gestalten.

Zunächst müssen Sie die Datei `tableformat.py` im WebIDE - Editor öffnen. Der Pfad zu dieser Datei lautet wie folgt:

```
/home/labex/project/tableformat.py
```

Sobald Sie die Datei geöffnet haben, sehen Sie die aktuelle Implementierung der Funktion `print_table()`. Diese Funktion ist dazu ausgelegt, tabellarische Daten zu formatieren und auszugeben. Sie nimmt zwei Hauptparameter entgegen: eine Liste von Datensätzen (die Objekte sind) und eine Liste von Feldnamen. Basierend auf diesen Eingaben gibt sie eine schön formatierte Tabelle aus.

Jetzt testen wir diese Funktion, um zu sehen, wie sie funktioniert. Öffnen Sie ein Terminal im WebIDE und führen Sie die folgenden Python - Befehle aus. Diese Befehle importieren die erforderlichen Module, lesen Daten aus einer CSV - Datei und verwenden dann die Funktion `print_table()`, um die Daten anzuzeigen.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Nachdem Sie diese Befehle ausgeführt haben, sollten Sie die folgende Ausgabe sehen:

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Die Ausgabe sieht gut aus, aber diese Funktion hat eine Einschränkung. Derzeit unterstützt sie nur ein Ausgabeformat, nämlich einfachen Text. In realen Szenarien möchten Sie möglicherweise Ihre Daten in verschiedenen Formaten wie CSV, HTML oder anderen ausgeben.

Anstatt die Funktion `print_table()` jedes Mal zu ändern, wenn wir ein neues Ausgabeformat unterstützen möchten, können wir Vererbung nutzen, um eine flexiblere Lösung zu schaffen. So werden wir vorgehen:

1. Wir definieren eine Basisklasse `TableFormatter`. Diese Klasse wird Methoden haben, die zur Formatierung von Daten verwendet werden. Die Basisklasse bietet eine gemeinsame Struktur und Funktionalität, auf der alle Unterklassen aufbauen können.
2. Wir erstellen verschiedene Unterklassen. Jede Unterklasse wird für ein anderes Ausgabeformat entworfen. Beispielsweise könnte eine Unterklasse für die CSV - Ausgabe, eine andere für die HTML - Ausgabe und so weiter verwendet werden. Diese Unterklassen erben die Methoden von der Basisklasse und können auch ihre eigene spezifische Funktionalität hinzufügen.
3. Wir ändern die Funktion `print_table()`, damit sie mit jedem Formatter arbeiten kann. Dies bedeutet, dass wir verschiedene Unterklassen der Klasse `TableFormatter` an die Funktion `print_table()` übergeben können, und sie wird in der Lage sein, die entsprechenden Formatierungsmethoden zu verwenden.

Dieser Ansatz hat einen großen Vorteil. Er ermöglicht es uns, neue Ausgabeformate hinzuzufügen, ohne die Kernfunktionalität der Funktion `print_table()` zu ändern. Wenn sich also Ihre Anforderungen ändern und Sie mehr Ausgabeformate unterstützen müssen, können Sie dies einfach tun, indem Sie neue Unterklassen erstellen.
