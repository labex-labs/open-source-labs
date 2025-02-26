# Übung 4.6: Verwenden von Vererbung, um verschiedene Ausgaben zu erzeugen

Die Klasse `TableFormatter`, die Sie im Teil (a) definiert haben, soll über die Vererbung erweitert werden. Tatsächlich ist das der ganze Gedanke. Um dies zu veranschaulichen, definieren Sie eine Klasse `TextTableFormatter` wie folgt:

```python
# tableformat.py
...
class TextTableFormatter(TableFormatter):
    '''
    Gibt eine Tabelle im einfachen - Text - Format aus
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 +' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

Ändern Sie die Funktion `portfolio_report()` wie folgt und testen Sie sie:

```python
# report.py
...
def portfolio_report(portfoliofile, pricefile):
    '''
    Erstellt einen Aktienbericht aus den Portfolio - und Preisdaten - Dateien.
    '''
    # Lese die Daten - Dateien
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Erstelle die Berichts - Daten
    report = make_report_data(portfolio, prices)

    # Drucke sie aus
    formatter = tableformat.TextTableFormatter()
    print_report(report, formatter)
```

Dies sollte die gleiche Ausgabe wie zuvor erzeugen:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

Ändern wir jedoch die Ausgabe in etwas anderes. Definieren Sie eine neue Klasse `CSVTableFormatter`, die die Ausgabe im CSV - Format erzeugt:

```python
# tableformat.py
...
class CSVTableFormatter(TableFormatter):
    '''
    Gibt Portfolio - Daten im CSV - Format aus.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

Ändern Sie Ihr Hauptprogramm wie folgt:

```python
def portfolio_report(portfoliofile, pricefile):
    '''
    Erstellt einen Aktienbericht aus den Portfolio - und Preisdaten - Dateien.
    '''
    # Lese die Daten - Dateien
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Erstelle die Berichts - Daten
    report = make_report_data(portfolio, prices)

    # Drucke sie aus
    formatter = tableformat.CSVTableFormatter()
    print_report(report, formatter)
```

Sie sollten jetzt die folgende CSV - Ausgabe sehen:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
```

Mit einem ähnlichen Ansatz definieren Sie eine Klasse `HTMLTableFormatter`, die eine Tabelle mit der folgenden Ausgabe erzeugt:

    <tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
    <tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
    <tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
    <tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
    <tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
    <tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
    <tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
    <tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>

Testen Sie Ihren Code, indem Sie das Hauptprogramm ändern, um ein `HTMLTableFormatter`-Objekt statt eines `CSVTableFormatter`-Objekts zu erstellen.
