# Erstellen einer Fabrikfunktion

Beim Verwenden von Vererbung besteht eine häufige Herausforderung darin, dass Benutzer sich die Namen der spezifischen Formatiererklassen merken müssen. Dies kann recht mühsam sein, insbesondere wenn die Anzahl der Klassen wächst. Um diesen Prozess zu vereinfachen, können wir eine Fabrikfunktion erstellen. Eine Fabrikfunktion ist eine spezielle Art von Funktion, die Objekte erstellt und zurückgibt. In unserem Fall wird sie den entsprechenden Formatierer basierend auf einem einfachen Formatnamen zurückgeben.

Fügen Sie die folgende Funktion zu Ihrer `tableformat.py` - Datei hinzu. Diese Funktion nimmt einen Formatnamen als Argument und gibt das entsprechende Formatiererobjekt zurück.

```python
def create_formatter(format_name):
    """
    Create a formatter of the specified type.

    Args:
        format_name: Name of the formatter ('text', 'csv', 'html')

    Returns:
        A TableFormatter object

    Raises:
        ValueError: If format_name is not recognized
    """
    if format_name == 'text':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
```

Die Funktion `create_formatter()` ist eine Fabrikfunktion. Sie überprüft das von Ihnen bereitgestellte Argument `format_name`. Wenn es 'text' ist, erstellt und gibt sie ein `TextTableFormatter` - Objekt zurück. Wenn es 'csv' ist, gibt sie ein `CSVTableFormatter` - Objekt zurück, und wenn es 'html' ist, gibt sie ein `HTMLTableFormatter` - Objekt zurück. Wenn der Formatname nicht erkannt wird, löst sie eine `ValueError` - Ausnahme aus. Auf diese Weise können Benutzer einen Formatierer einfach durch Angabe eines einfachen Namens auswählen, ohne die spezifischen Klassennamen kennen zu müssen.

Jetzt testen wir die Fabrikfunktion. Wir verwenden einige vorhandene Funktionen und Klassen, um Daten aus einer CSV - Datei zu lesen und sie in verschiedenen Formaten auszugeben.

```python
import stock
import reader
from tableformat import create_formatter, print_table

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Test with text formatter
formatter = create_formatter('text')
print("\nText Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with CSV formatter
formatter = create_formatter('csv')
print("\nCSV Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with HTML formatter
formatter = create_formatter('html')
print("\nHTML Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

In diesem Code importieren wir zunächst die erforderlichen Module und Funktionen. Dann lesen wir Daten aus der Datei `portfolio.csv` und erstellen ein `portfolio` - Objekt. Danach testen wir die Funktion `create_formatter()` mit verschiedenen Formatnamen: 'text', 'csv' und 'html'. Für jedes Format erstellen wir ein Formatiererobjekt, geben den Formatnamen aus und verwenden dann die Funktion `print_table()`, um die `portfolio` - Daten im angegebenen Format auszugeben.

Wenn Sie diesen Code ausführen, sollten Sie Ausgabe in allen drei Formaten sehen, getrennt durch den Formatnamen:

```
Text Format:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

CSV Format:
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44

HTML Format:
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

Die Fabrikfunktion macht den Code benutzerfreundlicher, da sie die Details der Klasseninstanzierung verbirgt. Benutzer müssen nicht wissen, wie man Formatiererobjekte erstellt; sie müssen nur das gewünschte Format angeben.

Dieses Muster des Verwenden einer Fabrikfunktion zur Objekterstellung ist ein gängiges Entwurfsmuster in der objektorientierten Programmierung, bekannt als Fabrikmuster (Factory Pattern). Es bietet eine Abstraktionsschicht zwischen dem Clientcode (dem Code, der den Formatierer verwendet) und den tatsächlichen Implementierungsklassen (den Formatiererklassen). Dies macht den Code modularer und einfacher zu verwenden.

**Wiederholung der Schlüsselkonzepte:**

1. **Abstrakte Basisklasse**: Die Klasse `TableFormatter` dient als Schnittstelle (Interface). Eine Schnittstelle definiert eine Reihe von Methoden, die alle Klassen, die sie implementieren, haben müssen. In unserem Fall müssen alle Formatiererklassen die in der Klasse `TableFormatter` definierten Methoden implementieren.

2. **Vererbung**: Die konkreten Formatiererklassen wie `TextTableFormatter`, `CSVTableFormatter` und `HTMLTableFormatter` erben von der Basisklasse `TableFormatter`. Dies bedeutet, dass sie die Grundstruktur und die Methoden von der Basisklasse erhalten und ihre eigenen spezifischen Implementierungen bereitstellen können.

3. **Polymorphismus**: Die Funktion `print_table()` kann mit jedem Formatierer arbeiten, der die erforderliche Schnittstelle implementiert. Dies bedeutet, dass Sie verschiedene Formatiererobjekte an die Funktion `print_table()` übergeben können, und sie wird korrekt mit jedem davon funktionieren.

4. **Fabrikmuster**: Die Funktion `create_formatter()` vereinfacht die Erstellung von Formatiererobjekten. Sie kümmert sich um die Details der Erstellung des richtigen Objekts basierend auf dem Formatnamen, sodass sich Benutzer nicht darum kümmern müssen.

Durch die Verwendung dieser objektorientierten Prinzipien haben wir ein flexibles und erweiterbares System zur Formatierung tabellarischer Daten in verschiedenen Ausgabeformaten erstellt.
