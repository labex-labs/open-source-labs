# Creación de un Jupyter Notebook e Importación de las Bibliotecas Requeridas

En la primera celda de tu cuaderno (notebook), introduce el siguiente código para importar las bibliotecas necesarias:

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
```

Vamos a entender qué hace cada una de estas bibliotecas:

- `matplotlib.pyplot` (con alias `plt`): Una colección de funciones que hace que matplotlib funcione como MATLAB, proporcionando una interfaz conveniente para crear gráficos.
- `numpy` (con alias `np`): Un paquete fundamental para la computación científica en Python, que usaremos para la manipulación de datos.
- `matplotlib.cbook`: Una colección de funciones de utilidad para matplotlib, incluyendo funciones para obtener datos de muestra.
- `matplotlib.image`: Un módulo para la funcionalidad relacionada con imágenes en matplotlib, que usaremos para leer y mostrar imágenes.

Ejecuta la celda haciendo clic en el botón "Run" en la parte superior del cuaderno o presionando Shift+Enter.

![libraries-imported](../assets/screenshot-20250306-18gJ6FRZ@2x.png)

La ejecución de esta celda debe completarse sin ningún resultado, lo que indica que todas las bibliotecas se importaron correctamente.
