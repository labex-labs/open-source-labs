# 2 つの軸を持つグラフを作成する

このステップでは、2 つの軸を持つグラフを作成します。`add_axes`メソッドを使用して、グラフに 2 つの軸を追加します。また、最初の軸の y 軸目盛りラベルと、2 番目の軸のタイトルを設定します。

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["very long label"])
ax1.set_ylabel("Y label")

ax2.set_title("Title")
```
