# 正弦波プロットの作成

まず、numpy と matplotlib ライブラリを使って正弦波プロットを作成する必要があります。

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
```
