# Define Dimensions

Define the dimensions of the box by creating three variables for the length of each side: Nx, Ny, and Nz. Then create three meshgrids for X, Y, and Z using numpy's arange method. Finally, set the negative value for Z to create a box instead of a plane.

```python
import matplotlib.pyplot as plt
import numpy as np

# Define dimensions
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
