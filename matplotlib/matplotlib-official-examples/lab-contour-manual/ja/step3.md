# グラフを作成する

次のステップは、グラフを作成することです。これは、ContourSet 関数を使用して行うことができます。

```python
fig, ax = plt.subplots()

# Filled contours using filled=True.
cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
cbar = fig.colorbar(cs)

# Contour lines (non-filled).
lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='User-specified contours')
```
