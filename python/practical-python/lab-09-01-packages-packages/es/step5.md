# Problema: Importaciones

Las importaciones entre archivos en el mismo paquete _ahora deben incluir el nombre del paquete en la importación_. Recuerda la estructura.

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Ejemplo de importación modificada.

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Todas las importaciones son _absolutas_, no relativas.

```python
import fileparse    # SE ROMPE. fileparse no se encuentra

...
```
