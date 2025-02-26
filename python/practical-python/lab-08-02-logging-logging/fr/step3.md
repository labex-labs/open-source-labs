# Utilisation de la journalisation

Le module `logging` peut résoudre ce problème.

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

Le code est modifié pour émettre des messages d'avertissement ou d'un objet `Logger` spécial. Celui créé avec `logging.getLogger(__name__)`.
