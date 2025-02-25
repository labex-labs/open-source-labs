# Habilitando la Copia al Escribir

Primero, habilitemos el CoW en pandas. Esto se puede hacer utilizando la opción de configuración `copy_on_write` en pandas. A continuación, se presentan dos maneras de habilitar el CoW de manera global.

```python
# Importando las bibliotecas pandas y numpy
import pandas as pd

# Habilitar el CoW utilizando set_option
pd.set_option("mode.copy_on_write", True)

# O utilizando una asignación directa
pd.options.mode.copy_on_write = True
```
