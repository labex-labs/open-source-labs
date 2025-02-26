# Übung 6.7: Beobachten Ihres Portfolios

Ändern Sie das Programm `follow.py` so, dass es den Strom von Aktiendaten beobachtet und einen Ticker druckt, der nur Informationen für die Aktien in einem Portfolio anzeigt. Beispielsweise:

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Hinweis: Damit dies funktioniert, muss Ihre `Portfolio`-Klasse den `in`-Operator unterstützen. Siehe Übung 6.3 und stellen Sie sicher, dass Sie den `__contains__()`-Operator implementieren.
