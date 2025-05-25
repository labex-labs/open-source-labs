# Exercício 9.3: Scripts de nível superior

Usar o comando `python -m` é frequentemente um pouco estranho. Você pode querer escrever um script de nível superior que simplesmente lida com as peculiaridades dos pacotes. Crie um script `print-report.py` que produza o relatório acima:

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

Coloque este script no diretório de nível superior `porty-app/`. Certifique-se de que você pode executá-lo nesse local:

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

Seu código final agora deve ser estruturado mais ou menos assim:

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
