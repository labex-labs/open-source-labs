# Определить размеры

Определите размеры куба, создав три переменные для длины каждой стороны: Nx, Ny и Nz. Затем создайте три сетки для X, Y и Z с использованием метода arange из библиотеки numpy. Наконец, задайте отрицательное значение для Z, чтобы создать куб, а не плоскость.

```python
import matplotlib.pyplot as plt
import numpy as np

# Define dimensions
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
