# Establecer rcParams en tiempo de ejecución

Puedes cambiar dinámicamente la configuración de configuración predeterminada en tiempo de ejecución en un script de Python o de forma interactiva desde la shell de Python. La variable `matplotlib.rcParams` es global para el paquete Matplotlib y almacena todas las configuraciones rc. Para personalizar los rcParams en tiempo de ejecución, puedes modificarlos directamente utilizando el diccionario `mpl.rcParams`. Aquí hay un ejemplo:

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

Este código cambia el ancho de línea predeterminado y el estilo de línea para todas las gráficas creadas con Matplotlib.

Veamos algunos datos aleatorios trazados con los nuevos ajustes predeterminados.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```
