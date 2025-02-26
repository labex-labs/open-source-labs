# Tabellenausgabe

In Übung 3.1 haben Sie eine Funktion `print_portfolio()` geschrieben, die eine schön formattierte Tabelle erstellt. Diese Funktion war speziell auf eine Liste von `Stock`-Objekten zugeschnitten. Mit der Technik aus Teil (b) kann jedoch die Funktion vollständig verallgemeinert werden, um mit jeder Liste von Objekten zu arbeiten.

Erstellen Sie ein neues Modul namens `tableformat.py`. Schreiben Sie in diesem Programm eine Funktion `print_table()`, die eine Sequenz (Liste) von Objekten und eine Liste von Attributnamen übernimmt und eine schön formattierte Tabelle ausgibt. Beispielsweise:

```python
>>> import stock
>>> import tableformat
>>> portfolio = stock.read_portfolio('portfolio.csv')
>>> tableformat.print_table(portfolio, ['name','shares','price'])
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

>>> tableformat.print_table(portfolio,['shares','name'])
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
>>>
```

Um es einfach zu halten, soll die Funktion `print_table()` jedes Feld in einer 10-zeichenweiten Spalte ausgeben.
