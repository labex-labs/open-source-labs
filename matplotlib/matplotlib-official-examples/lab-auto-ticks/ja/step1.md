# round_numbers オートリミットモードなしの散布図

このステップでは、round_numbers オートリミットモードなしで散布図を作成し、目盛りの自動配置の動作を観察します。

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```
