# Weiter so

Oh, du kannst das besser machen. Lassen Sie uns das in Ihren Tabellenerzeugungscode einfügen. Ändern Sie das Programm wie folgt:

```python
# ticker.py
...

if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name','price','change'], formatter)
```

Dies sollte eine Ausgabe erzeugen, die so aussieht:

          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19

Jetzt ist das verrückt! Und ziemlich fantastisch.

**Diskussion**

Einige Lehren, die man ziehen kann: Man kann verschiedene Generatorfunktionen erstellen und sie miteinander verketten, um Verarbeitungen durchzuführen, die Datenflussleitungen betreffen.

Ein guter Denkmodell für Generatorfunktionen könnte Lego-Blöcke sein. Man kann eine Sammlung kleiner Iterator-Muster erstellen und sie auf verschiedene Weise zusammen stapeln. Es kann ein extrem leistungsfähiger Weg der Programmierung sein.
