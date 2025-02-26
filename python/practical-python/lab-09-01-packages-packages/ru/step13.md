# Упражнение 9.3: Верхнеуровневые скрипты

Использование команды `python -m` часто выглядит несколько странно. Возможно, вы захотите написать верхнеуровневый скрипт, который просто будет обрабатывать специфические аспекты пакетов. Создайте скрипт `print-report.py`, который генерирует вышеупомянутый отчет:

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

Разместите этот скрипт в верхнем уровне директории `porty-app/`. Убедитесь, что вы можете запустить его в этом месте:

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

Ваш окончательный код теперь должен быть структурирован примерно так:

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
