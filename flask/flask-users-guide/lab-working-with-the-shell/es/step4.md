# Mejora la experiencia de la shell

Para mejorar la experiencia de la shell, crea un módulo (`shelltools.py`) con métodos auxiliares que se pueden importar en la sesión interactiva. Este módulo puede contener métodos auxiliares adicionales para tareas como la inicialización de la base de datos o la eliminación de tablas.

```python
# Archivo: shelltools.py

def initialize_database():
    # Código para inicializar la base de datos
    pass

def drop_tables():
    # Código para eliminar tablas
    pass
```

En la shell interactiva, importa los métodos deseados del módulo `shelltools`.

```python
# Archivo: shell.py
# Ejecución: python shell.py

from shelltools import initialize_database, drop_tables

# Importa los métodos deseados del módulo shelltools
from shelltools import *

# Utiliza los métodos importados
initialize_database()
drop_tables()
```
