# 2 つの調整可能な軸を持つグラフを作成する

このステップでは、2 つの調整可能な軸を持つグラフを作成します。軸を調整できるようにするディバイダを作成するために`make_axes_locatable`メソッドを使用します。`append_axes`メソッドを使って、最初の軸の右に新しい軸を追加します。

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
