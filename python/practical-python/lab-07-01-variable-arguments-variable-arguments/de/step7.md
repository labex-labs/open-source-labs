# Übung 7.3: Erstellen einer Liste von Instanzen

In Ihrem `report.py`-Programm haben Sie eine Liste von Instanzen mit Code wie diesem erstellt:

```python
def read_portfolio(filename):
    '''
    Liest eine Datei mit einem Aktienportfolio in eine Liste von Wörterbüchern mit den Schlüsseln
    name, shares und price ein.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                               select=['name','shares','price'],
                               types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts ]
    return Portfolio(portfolio)
```

Sie können diesen Code vereinfachen, indem Sie `Stock(**d)` verwenden. Machen Sie diese Änderung.
