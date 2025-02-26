# Переменные окружения

Переменные окружения настраиваются в оболочке.

```bash
$ export NAME dave
$ export RSH ssh
$ python3 prog.py
```

`os.environ` - это словарь, содержащий эти значения.

```python
import os

name = os.environ['NAME'] # 'dave'
```

Изменения отражаются в любых дочерних процессах, запускаемых программой позже.
