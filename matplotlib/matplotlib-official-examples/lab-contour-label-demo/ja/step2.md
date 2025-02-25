# カスタムレベルフォーマッタを使って等高線ラベルを作成する

次に、カスタムレベルフォーマッタを使って等高線ラベルを作成します。これにより、特定の方法でラベルをフォーマットすることができます。この場合、末尾のゼロを削除してパーセント記号を追加します。

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```
