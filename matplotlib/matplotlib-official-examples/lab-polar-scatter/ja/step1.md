# 必要なライブラリをインポートする

極座標軸上に散布図を作成するには、Matplotlib と NumPy のライブラリをインポートする必要があります。再現性のために乱数シードも設定します。

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
```
