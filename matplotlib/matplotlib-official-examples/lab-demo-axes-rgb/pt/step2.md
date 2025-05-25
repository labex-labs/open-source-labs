# Definir uma função para obter os canais RGB

Nesta etapa, definiremos uma função `get_rgb()` para obter os canais R, G e B de uma imagem. Neste exemplo, usaremos a função `get_sample_data()` do módulo `cbook` para obter uma imagem de amostra.

```python
import matplotlib.cbook as cbook

def get_rgb():
    # Get a sample image
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # Get R, G, and B channels
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
