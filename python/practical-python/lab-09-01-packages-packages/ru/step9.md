# Другой способ запуска скриптов

Как уже упоминалось, теперь для запуска скриптов внутри пакета нужно использовать `-m package.module`.

```bash
$ python3 -m porty.pcost portfolio.csv
```

Есть другой вариант: написать новый верхнеуровневый скрипт.

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

Этот скрипт находится _за пределами_ пакета. Например, рассмотрим структуру каталогов:

    pcost.py       # верхнеуровневый скрипт
    porty/         # каталог пакета
        __init__.py
        pcost.py
     ...
