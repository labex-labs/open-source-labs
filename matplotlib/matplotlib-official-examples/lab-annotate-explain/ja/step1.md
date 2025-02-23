# プロットの設定

まず、2 つのサブプロットでプロットを設定する必要があります。`subplots` 関数を使って 2x2 のサブプロットのグリッドを作成し、その後、2 点の x 座標と y 座標を定義します。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
