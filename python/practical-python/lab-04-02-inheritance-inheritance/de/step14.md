# Übung 4.7: Polymorphismus in der Anwendung

Ein wichtiges Merkmal der objektorientierten Programmierung ist, dass Sie ein Objekt in ein Programm einfügen können und es funktioniert, ohne dass Sie den vorhandenen Code ändern müssen. Beispielsweise würde ein Programm, das erwartet, ein `TableFormatter`-Objekt zu verwenden, funktionieren, unabhängig davon, welchem `TableFormatter` Sie es tatsächlich geben. Dieses Verhalten wird manchmal als "Polymorphismus" bezeichnet.

Ein potenzielles Problem besteht darin, herauszufinden, wie es möglich ist, dass ein Benutzer den Formatter auswählt, den er möchte. Das direkte Verwenden von Klassennamen wie `TextTableFormatter` ist oft störend. Daher könnten Sie einen vereinfachten Ansatz in Betracht ziehen. Vielleicht integrieren Sie eine `if`-Anweisung in den Code wie folgt:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Erstellt einen Aktienbericht aus den Portfolio - und Preisdaten - Dateien.
    '''
    # Lese die Daten - Dateien
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Erstelle die Berichts - Daten
    report = make_report_data(portfolio, prices)

    # Drucke sie aus
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    print_report(report, formatter)
```

In diesem Code gibt der Benutzer einen vereinfachten Namen wie `'txt'` oder `'csv'` an, um ein Format auszuwählen. Ist es jedoch die beste Idee, eine große `if`-Anweisung in der Funktion `portfolio_report()` so zu platzieren? Es wäre vielleicht besser, diesen Code an eine allgemeine Funktion an einem anderen Ort zu verschieben.

In der Datei `tableformat.py` fügen Sie eine Funktion `create_formatter(name)` hinzu, die es einem Benutzer ermöglicht, einen Formatter anhand eines Ausgabennamens wie `'txt'`, `'csv'` oder `'html'` zu erstellen. Ändern Sie `portfolio_report()` so, dass es wie folgt aussieht:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Erstellt einen Aktienbericht aus den Portfolio - und Preisdaten - Dateien.
    '''
    # Lese die Daten - Dateien
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Erstelle die Berichts - Daten
    report = make_report_data(portfolio, prices)

    # Drucke sie aus
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

Testen Sie die Funktion mit verschiedenen Formaten, um sicherzustellen, dass sie funktioniert.
