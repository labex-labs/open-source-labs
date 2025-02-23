# ライブラリのインポートとデータの設定

まず、必要なライブラリをインポートし、プロットするためのいくつかのデータを設定する必要があります。この例では、いくつかのランダムノイズが加えられた3つのサイン波をプロットします。

```python
import matplotlib.pyplot as plt
import numpy as np

# Set up data
np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))
```
