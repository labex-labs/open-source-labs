# Übung 4.5: Ein Problem mit der Erweiterbarkeit

Angenommen, Sie möchten die Funktion `print_report()` so ändern, dass sie verschiedene Ausgabeformate wie einfachen Text, HTML, CSV oder XML unterstützt. Um dies zu tun, könnten Sie versuchen, eine riesige Funktion zu schreiben, die alles macht. Dies würde jedoch wahrscheinlich zu einem unhaltbaren Durcheinander führen. Stattdessen ist dies eine perfekte Gelegenheit, die Vererbung zu verwenden.

Beginnen Sie mit den Schritten, die bei der Erstellung einer Tabelle beteiligt sind. Am Anfang der Tabelle befindet sich eine Reihe von Tabellenüberschriften. Danach erscheinen die Zeilen der Tabellendaten. Nehmen wir diese Schritte und bringen Sie sie in ihre eigene Klasse. Erstellen Sie eine Datei namens `tableformat.py` und definieren Sie die folgende Klasse:

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Gibt die Tabellenüberschriften aus.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Gibt eine einzelne Zeile der Tabellendaten aus.
        '''
        raise NotImplementedError()
```

Diese Klasse tut nichts, aber sie dient als Art von Entwurfspezifikation für zusätzliche Klassen, die bald definiert werden. Eine Klasse wie diese wird manchmal als "abstrakte Basisklasse" bezeichnet.

Ändern Sie die Funktion `print_report()`, so dass sie ein `TableFormatter`-Objekt als Eingabe akzeptiert und auf diesem Methoden aufruft, um die Ausgabe zu erzeugen. Beispielsweise wie folgt:

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    Druckt eine schön formattierte Tabelle aus einer Liste von (Name, Anteile, Preis, Änderung) - Tupeln.
    '''
    formatter.headings(['Name','Anteile','Preis','Änderung'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

Da Sie einem Argument in `print_report()` hinzugefügt haben, müssen Sie auch die Funktion `portfolio_report()` ändern. Ändern Sie sie so, dass sie einen `TableFormatter` wie folgt erstellt:

```python
# report.py

import tableformat

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
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

Führen Sie diesen neuen Code aus:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... stürzt ab...
```

Es sollte sofort mit einer `NotImplementedError`-Ausnahme abstürzen. Das ist nicht sehr aufregend, aber genau das, was wir erwartet haben. Fortfahren Sie mit dem nächsten Teil.
