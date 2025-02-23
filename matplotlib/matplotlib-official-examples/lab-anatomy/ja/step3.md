# データのプロット

次に、先ほど作成した軸にデータをプロットします。異なる色と線幅で3つのサイン波をプロットするには、`plot()` メソッドを使用します。

```python
# Plot data
ax.plot(X, Y1, c='C0', lw=2.5, label="Blue signal", zorder=10)
ax.plot(X, Y2, c='C1', lw=2.5, label="Orange signal")
ax.plot(X[::3], Y3[::3], linewidth=0, markersize=9,
        marker='s', markerfacecolor='none', markeredgecolor='C4',
        markeredgewidth=2.5)
```
