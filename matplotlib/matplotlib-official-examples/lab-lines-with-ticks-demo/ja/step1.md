# ライブラリのインポートとデータの生成

まず、必要なライブラリをインポートして、描画用のデータを生成します。

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

# Generate data
nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
```
