# Variables de entorno

Las variables de entorno se establecen en la shell.

```bash
$ export NAME dave
$ export RSH ssh
$ python3 prog.py
```

`os.environ` es un diccionario que contiene estos valores.

```python
import os

name = os.environ['NAME'] # 'dave'
```

Los cambios se reflejan en cualquier subproceso lanzado posteriormente por el programa.
