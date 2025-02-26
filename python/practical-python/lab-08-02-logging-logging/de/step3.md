# Das Verwenden von Protokollierung

Das `Protokollierungsmodul` kann dies beheben.

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

Der Code wird geändert, um Warnmeldungen auszugeben oder ein spezielles `Logger`-Objekt. Das mit `logging.getLogger(__name__)` erstellte.
