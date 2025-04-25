# データをプロットする

ここでは、Matplotlib の pyplot モジュールを使って mu 対 sigma をプロットします。計算された mu と sigma の値を使って散布図を作成します。また、`picker`パラメータを True に設定することで、プロットにインタラクティビティを追加します。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```
