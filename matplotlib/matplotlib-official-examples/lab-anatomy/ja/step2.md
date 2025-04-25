# グラフの作成と軸の設定

次に、グラフを作成して軸を設定します。`add_axes()` メソッドを使用して、グラフ内に新しい軸のセットを作成します。また、x 軸と y 軸の範囲を設定し、グリッド線を追加します。

```python
# Create figure and axes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Set limits and gridlines
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```
