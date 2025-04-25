# 中心座標

ユーザーは、`.axes.Axes.pcolormesh`に対して、*X*と*Y*を*Z*と同じサイズで渡したい場合が多いです。`shading='auto'`を渡す場合（:rc:`pcolor.shading`による既定の設定）もこれは許可されます。Matplotlib 3.3 以前では、`shading='flat'`では*Z*の最後の列と行が削除されましたが、現在はエラーが発生します。これが本当に必要な場合、簡単に*Z*の最後の行と列を手動で削除してください：

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(10)  # len = 10
y = np.arange(6)  # len = 6
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z),
                  shading='flat')
axs[1].set_title("shading='flat'")
```
