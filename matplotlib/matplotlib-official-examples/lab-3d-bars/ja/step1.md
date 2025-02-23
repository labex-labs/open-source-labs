# ライブラリのインポートとグラフの設定

最初のステップでは、必要なライブラリをインポートし、チャート用のグラフと軸を設定します。

```python
import matplotlib.pyplot as plt
import numpy as np

# set up the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
```
