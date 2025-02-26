# Ejercicio 9.3: Scripts de nivel superior

Usar el comando `python -m` a menudo es un poco extraño. Es posible que desees escribir un script de nivel superior que simplemente gestione las particularidades de los paquetes. Crea un script `print-report.py` que genere el informe anterior:

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

Coloca este script en el directorio principal `porty-app/`. Asegúrate de que puedas ejecutarlo en esa ubicación:

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

Tu código final ahora debería estar estructurado de algo así:

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
