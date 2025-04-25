# ライブラリのインポートとデータの生成

まず、必要なライブラリをインポートして、使用するサンプルデータを生成する必要があります。この例では、データの生成に numpy を、可視化に matplotlib を使用します。

```python
import matplotlib.pyplot as plt
import numpy as np

# example data
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# example variable error bar values
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
