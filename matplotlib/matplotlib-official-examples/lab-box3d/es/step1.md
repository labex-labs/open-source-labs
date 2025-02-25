# Define dimensiones

Define las dimensiones de la caja creando tres variables para la longitud de cada lado: Nx, Ny y Nz. Luego, crea tres mallas bidimensionales para X, Y y Z utilizando el método arange de numpy. Finalmente, establece un valor negativo para Z para crear una caja en lugar de un plano.

```python
import matplotlib.pyplot as plt
import numpy as np

# Define dimensiones
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
