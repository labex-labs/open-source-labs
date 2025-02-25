# データをプロットする

ここでは、Matplotlibのpyplotモジュールを使ってmu対sigmaをプロットします。計算されたmuとsigmaの値を使って散布図を作成します。また、`picker`パラメータをTrueに設定することで、プロットにインタラクティビティを追加します。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```
