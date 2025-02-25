# Dimensionen definieren

Definieren Sie die Dimensionen der Box, indem Sie drei Variablen für die Länge jeder Seite erstellen: Nx, Ny und Nz. Erstellen Sie dann drei Gitternetze für X, Y und Z mit der arange-Methode von numpy. Legen Sie schließlich den negativen Wert für Z fest, um eine Box statt einer Ebene zu erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np

# Define dimensions
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
