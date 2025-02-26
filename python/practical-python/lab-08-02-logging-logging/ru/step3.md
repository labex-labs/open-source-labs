# Использование журналирования

Модуль `logging` может решить эту проблему.

```python
# fileparse.py
import logging
log = logging.getLogger(__name__)

def parse(f,types=None,names=None,delimiter=None):
 ...
    try:
        records.append(split(line,types,names,delimiter))
    except ValueError as e:
        log.warning("Couldn't parse : %s", line)
        log.debug("Reason : %s", e)
```

Код модифицирован для вывода сообщений об ошибках или с использованием специального объекта `Logger`. Создается с помощью `logging.getLogger(__name__)`.
