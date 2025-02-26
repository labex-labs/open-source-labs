# El depurador de Python

Puedes lanzar manualmente el depurador dentro de un programa.

```python
def some_function():
 ...
    breakpoint()      # Entra al depurador (Python 3.7+)
 ...
```

Esto inicia el depurador en la llamada a `breakpoint()`.

En versiones anteriores de Python, se hacía así. A veces verás esto mencionado en otras guías de depuración.

```python
import pdb
...
pdb.set_trace()       # En lugar de `breakpoint()`
...
```
