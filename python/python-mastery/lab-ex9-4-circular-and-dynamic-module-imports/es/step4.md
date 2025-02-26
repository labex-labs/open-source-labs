# Importaciones dinámicas

Ahora estás listo para la última frontera. Elimina por completo las siguientes declaraciones de importación:

```python
# formatter.py
...

from.formats.text import TextTableFormatter     # ELIMINA
from.formats.csv import CSVTableFormatter       # ELIMINA
from.formats.html import HTMLTableFormatter     # ELIMINA
...
```

Ejecuta nuevamente tu código `stock.py`; debería fallar con un error. No sabe nada del formateador de texto. Corrige esto agregando este pequeño fragmento de código a `create_formatter()`:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
  ...
```

Este código intenta una importación dinámica de un módulo de formateador si no se conoce nada del nombre. La importación sola (si funciona) registrará la clase con el diccionario `_formats` y todo funcionará. ¡Magia!

Intenta ejecutar el código `stock.py` y asegúrate de que funcione después.
