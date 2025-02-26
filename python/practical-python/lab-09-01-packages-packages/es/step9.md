# Otra solución para los scripts

Como se ha señalado, ahora debes usar `-m package.module` para ejecutar scripts dentro de tu paquete.

```bash
$ python3 -m porty.pcost portfolio.csv
```

Hay otra alternativa: Escribe un nuevo script de nivel superior.

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

Este script se encuentra _fuera_ del paquete. Por ejemplo, mirando la estructura de directorios:

    pcost.py       # script de nivel superior
    porty/         # directorio del paquete
        __init__.py
        pcost.py
     ...
