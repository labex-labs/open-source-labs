# Matplotlibをインポートする

Matplotlibを使ってグラフに注釈を付ける前に、まずライブラリをインポートする必要があります。このステップでは、Matplotlibをインポートして、注釈に使用する単純なグラフを作成します。

```python
import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```
