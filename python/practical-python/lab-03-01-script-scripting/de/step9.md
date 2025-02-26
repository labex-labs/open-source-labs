# Doc Strings

Es ist eine gute Praxis, Dokumentation in Form eines Doc-Strings beizubehalten. Doc-Strings sind Strings, die direkt nach dem Funktionsnamen geschrieben werden. Sie werden von `help()`, IDEs und anderen Tools verwendet.

```python
def read_prices(filename):
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

Eine gute Praxis für Doc-Strings ist es, einen kurzen einen-Satz-Zusammenfassung darüber zu schreiben, was die Funktion macht. Wenn weitere Informationen erforderlich sind, fügen Sie ein kurzes Verwendungsexempel zusammen mit einer detaillierteren Beschreibung der Argumente hinzu.
