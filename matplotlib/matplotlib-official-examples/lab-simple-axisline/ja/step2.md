# グラフとサブプロットの作成

次に、グラフを作成し、AxesZero を使ってサブプロットを追加します。これにより、x 軸と y 軸のラベル付きの軸線が作成されますが、目盛りやグリッドはありません。

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```
