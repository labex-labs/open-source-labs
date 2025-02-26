# Usando registro

El módulo `logging` puede resolver esto.

```python
# fileparse.py
import logging
log = logging.getLogger(__name__)

def parse(f,types=None,names=None,delimiter=None):
 ...
    try:
        records.append(split(line,types,names,delimiter))
    except ValueError as e:
        log.warning("No se pudo analizar : %s", line)
        log.debug("Razón : %s", e)
```

El código se modifica para emitir mensajes de advertencia o un objeto `Logger` especial. El creado con `logging.getLogger(__name__)`.
