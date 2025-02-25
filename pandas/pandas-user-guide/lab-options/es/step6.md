# Establecer Opciones de Inicio

Podemos crear un script de inicio en el entorno de Python/IPython para importar pandas y establecer opciones, lo que hace que trabajar con pandas sea más eficiente.

```python
# Este es un ejemplo de un script de inicio
# Coloca esto en un archivo.py en el directorio de inicio del perfil de IPython
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```
