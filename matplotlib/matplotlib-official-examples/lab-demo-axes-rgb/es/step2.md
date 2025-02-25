# Definir una función para obtener los canales RGB

En este paso, definiremos una función `get_rgb()` para obtener los canales R, G y B de una imagen. En este ejemplo, usaremos la función `get_sample_data()` del módulo `cbook` para obtener una imagen de muestra.

```python
import matplotlib.cbook as cbook

def get_rgb():
    # Obtener una imagen de muestra
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # Obtener los canales R, G y B
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
