# Importaciones Relativas

En lugar de usar directamente el nombre del paquete, puedes usar `.` para referirte al paquete actual.

```python
from. import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Sintaxis:

```python
from. import modname
```

Esto facilita renombrar el paquete.
