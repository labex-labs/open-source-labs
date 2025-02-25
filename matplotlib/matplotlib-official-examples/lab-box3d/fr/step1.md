# Définir les dimensions

Définissez les dimensions de la boîte en créant trois variables pour la longueur de chaque côté : Nx, Ny et Nz. Ensuite, créez trois maillages pour X, Y et Z à l'aide de la méthode arange de numpy. Enfin, définissez la valeur négative pour Z pour créer une boîte au lieu d'un plan.

```python
import matplotlib.pyplot as plt
import numpy as np

# Définir les dimensions
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
