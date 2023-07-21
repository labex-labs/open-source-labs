# Using logging

The `logging` module can address this.

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

The code is modified to issue warning messages or a special `Logger`
object. The one created with `logging.getLogger(__name__)`.
