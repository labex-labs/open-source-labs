# 定义尺寸

通过为每条边的长度创建三个变量来定义盒子的尺寸：Nx、Ny 和 Nz。然后使用 numpy 的 arange 方法为 X、Y 和 Z 创建三个网格。最后，为 Z 设置负值以创建一个盒子而不是一个平面。

```python
import matplotlib.pyplot as plt
import numpy as np

# 定义尺寸
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
