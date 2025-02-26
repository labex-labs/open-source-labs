# Übung 9.3: Oberste Ebene Skripte

Das Verwenden des Befehls `python -m` ist oft etwas ungewöhnlich. Möglicherweise möchten Sie ein oberstes Ebene Skript schreiben, das einfach mit den Besonderheiten von Paketen umgeht. Erstellen Sie ein Skript `print-report.py`, das den obigen Bericht erzeugt:

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

Legen Sie dieses Skript im obersten Level-Verzeichnis `porty-app/` ab. Stellen Sie sicher, dass Sie es an diesem Ort ausführen können:

    $ cd porty-app
    $ python3 print-report.py portfolio.csv prices.csv txt
          Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

    $

Ihr endgültiger Code sollte jetzt ungefähr so strukturiert sein:

    porty-app/
        portfolio.csv
        prices.csv
        print-report.py
        README.txt
        porty/
            __init__.py
            fileparse.py
            follow.py
            pcost.py
            portfolio.py
            report.py
            stock.py
            tableformat.py
            ticker.py
            typedproperty.py
