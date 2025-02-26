# Übung 7.4: Argumentweiterleitung

Die `fileparse.parse_csv()`-Funktion hat einige Optionen zur Änderung des Dateiteilnehmers und zur Fehlerberichterstattung. Vielleicht möchten Sie diese Optionen der obigen `read_portfolio()`-Funktion zur Verfügung stellen. Machen Sie diese Änderung:

    def read_portfolio(filename, **opts):
        '''
        Liest eine Datei mit einem Aktienportfolio in eine Liste von Wörterbüchern mit den Schlüsseln
        name, shares und price ein.
        '''
        with open(filename) as lines:
            portdicts = fileparse.parse_csv(lines,
                                            select=['name','shares','price'],
                                            types=[str,int,float],
                                            **opts)

        portfolio = [ Stock(**d) for d in portdicts ]
        return Portfolio(portfolio)

Sobald Sie die Änderung vorgenommen haben, versuchen Sie, eine Datei mit einigen Fehlern zu lesen:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv')
Zeile 4: Konvertierung von ['MSFT', '', '51.23'] fehlgeschlagen
Zeile 4: Grund ungültiger Buchstabe für int() mit Basis 10: ''
Zeile 7: Konvertierung von ['IBM', '', '70.44'] fehlgeschlagen
Zeile 7: Grund ungültiger Buchstabe für int() mit Basis 10: ''
>>>
```

Jetzt versuchen Sie, die Fehler zu unterdrücken:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv', silence_errors=True)
>>>
```
