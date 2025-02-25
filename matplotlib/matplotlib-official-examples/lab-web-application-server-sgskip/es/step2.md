# Importar dependencias

En este paso, importaremos las dependencias necesarias. Usaremos `base64` para codificar los datos de la imagen, `BytesIO` para almacenar los datos de la imagen en memoria, `Flask` para crear el servidor de aplicaciones web y `Figure` para crear las figuras.

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```
