# Triangulation オブジェクトを作成する

まず、Triangulation オブジェクトを作成する必要があります。`matplotlib.tri`から`Triangulation`クラスを使用します。この例では、ランダムなデータで Triangulation オブジェクトを作成します。

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Generate random data
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
