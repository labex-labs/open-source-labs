# Typ-Annotationen

Sie können auch optionale Typhinweise zu Funktionsdefinitionen hinzufügen.

```python
def read_prices(filename: str) -> dict:
    '''
    Liest Preise aus einer CSV-Datei mit Namen,Preis-Daten
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Die Hinweise haben keinerlei operative Wirkung. Sie sind rein informativ. Sie können jedoch von IDEs, Code-Checkern und anderen Tools genutzt werden, um mehr zu tun.

Im Abschnitt 2 haben Sie ein Programm namens `report.py` geschrieben, das einen Bericht ausdruckte, der die Leistung eines Aktienportfolios zeigt. Dieses Programm bestand aus einigen Funktionen. Beispielsweise:

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    Liest eine Aktienportfoliodatei in eine Liste von Dictionaries mit den Schlüsseln
    name, shares und price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
               'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

Es gab jedoch auch Teile des Programms, die einfach eine Reihe von skriptbasierten Berechnungen vornahmen. Dieser Code erschien am Ende des Programms. Beispielsweise:

```python
...

# Ausgabe des Berichts

headers = ('Name', 'Anteile', 'Preis', 'Änderung')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 +'') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

In dieser Übung werden wir dieses Programm nehmen und es etwas stärker um die Verwendung von Funktionen organisieren.
