# Comprender Matplotlib y crear un cuaderno (notebook)

En este primer paso, aprenderemos sobre Matplotlib y crearemos un nuevo cuaderno (Jupyter notebook) para nuestra tarea de visualización.

## ¿Qué es Matplotlib?

Matplotlib es una biblioteca integral para crear visualizaciones estáticas, animadas e interactivas en Python. Proporciona una interfaz de programación de aplicaciones (API) orientada a objetos para incrustar gráficos en aplicaciones y es ampliamente utilizada para la visualización de datos por científicos, ingenieros y analistas de datos.

## Crear un nuevo cuaderno (notebook)

En la primera celda de tu cuaderno, importemos la biblioteca Matplotlib. Escribe el siguiente código y ejecuta la celda presionando Shift+Enter:

```python
import matplotlib.pyplot as plt
import numpy as np

# Check the Matplotlib version
print(f"NumPy version: {np.__version__}")
```

![libraries-imported](../assets/screenshot-20250306-K6iIFfj1@2x.png)

Cuando ejecutes este código, deberías ver una salida similar a la siguiente:

```
NumPy version: 2.0.0
```

El número exacto de la versión puede variar dependiendo de tu entorno.

Ahora tenemos Matplotlib importado y listo para usar. `plt` es un alias convencional utilizado para el módulo pyplot, que proporciona una interfaz similar a MATLAB para crear gráficos.
