# Erstellen zusätzlicher Formatierer

In der Programmierung ist Vererbung (inheritance) ein mächtiges Konzept, das es uns ermöglicht, neue Klassen auf der Grundlage bestehender zu erstellen. Dies hilft bei der Wiederverwendung von Code und macht unsere Programme erweiterbarer. In diesem Teil des Experiments werden wir Vererbung nutzen, um zwei neue Formatierer für verschiedene Ausgabeformate zu erstellen: CSV und HTML. Diese Formatierer werden von einer Basisklasse erben, was bedeutet, dass sie einige gemeinsame Verhaltensweisen teilen, während sie ihre eigenen einzigartigen Methoden zur Datenformatierung haben.

Jetzt fügen wir die folgenden Klassen zu Ihrer `tableformat.py` - Datei hinzu. Diese Klassen werden definieren, wie Daten in CSV - und HTML - Formaten formatiert werden sollen.

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

Die Klasse `CSVTableFormatter` ist dafür konzipiert, Daten im CSV - Format (Comma - Separated Values, Komma - getrennte Werte) zu formatieren. Die Methode `headings` nimmt eine Liste von Überschriften und gibt sie getrennt durch Kommas aus. Die Methode `row` nimmt eine Liste von Daten für eine einzelne Zeile und gibt sie ebenfalls getrennt durch Kommas aus.

Die Klasse `HTMLTableFormatter` hingegen wird verwendet, um HTML - Tabellen - Code zu generieren. Die Methode `headings` erstellt die Tabellenüberschriften mit HTML - `<th>` - Tags, und die Methode `row` erstellt eine Tabellenzeile mit HTML - `<td>` - Tags.

Testen wir diese neuen Formatierer, um zu sehen, wie sie funktionieren.

1. Zuerst testen wir den CSV - Formatierer:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

In diesem Code importieren wir zunächst die erforderlichen Module. Dann lesen wir Daten aus einer CSV - Datei namens `portfolio.csv` und erstellen Instanzen der Klasse `Stock`. Als Nächstes erstellen wir eine Instanz der Klasse `CSVTableFormatter`. Schließlich verwenden wir die Funktion `print_table`, um die Portfolio - Daten im CSV - Format auszugeben.

Sie sollten die folgende CSV - formatierte Ausgabe sehen:

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. Jetzt testen wir den HTML - Formatierer:

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Hier erstellen wir eine Instanz der Klasse `HTMLTableFormatter` und verwenden erneut die Funktion `print_table`, um die Portfolio - Daten im HTML - Format auszugeben.

Sie sollten die folgende HTML - formatierte Ausgabe sehen:

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

Wie Sie sehen können, erzeugt jeder Formatierer Ausgabe in einem anderen Format, aber sie alle teilen die gleiche Schnittstelle, die von der Basisklasse `TableFormatter` definiert wird. Dies ist ein großartiges Beispiel für die Macht von Vererbung und Polymorphismus. Wir können Code schreiben, der mit der Basisklasse arbeitet, und er wird automatisch mit jeder Unterklasse funktionieren.

Die Funktion `print_table()` muss nichts über den spezifischen verwendeten Formatierer wissen. Sie ruft einfach die in der Basisklasse definierten Methoden auf, und die entsprechende Implementierung wird basierend auf der Art des bereitgestellten Formatierers ausgewählt. Dies macht unseren Code flexibler und leichter zu warten.
