# Definir Dimensões

Defina as dimensões da caixa criando três variáveis para o comprimento de cada lado: Nx, Ny e Nz. Em seguida, crie três meshgrids para X, Y e Z usando o método arange do numpy. Finalmente, defina o valor negativo para Z para criar uma caixa em vez de um plano.

```python
import matplotlib.pyplot as plt
import numpy as np

# Define dimensions
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
