# 寸法を定義する

各辺の長さに対して 3 つの変数 Nx、Ny、Nz を作成することで、ボックスの寸法を定義します。次に、numpy の arange メソッドを使って X、Y、Z の 3 つのメッシュグリッドを作成します。最後に、平面ではなくボックスを作成するために、Z に負の値を設定します。

```python
import matplotlib.pyplot as plt
import numpy as np

# Define dimensions
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
