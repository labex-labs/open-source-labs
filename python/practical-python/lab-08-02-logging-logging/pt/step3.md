# Usando `logging`

O módulo `logging` pode resolver isso.

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

O código é modificado para emitir mensagens de aviso ou um objeto `Logger` especial. Aquele criado com `logging.getLogger(__name__)`.
