# Umgebungsvariablen

Umgebungsvariablen werden in der Shell festgelegt.

```bash
$ export NAME dave
$ export RSH ssh
$ python3 prog.py
```

`os.environ` ist ein Wörterbuch, das diese Werte enthält.

```python
import os

name = os.environ['NAME'] # 'dave'
```

Änderungen werden in allen späteren von dem Programm gestarteten Unterprozessen widergespiegelt.
