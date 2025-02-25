# 上限と下限を追加する

エラーバーに上限と下限の両方を追加するには、`errorbar`関数の`uplims`と`lolims`の両方のパラメータを使用します。また、このプロットと前のプロットを区別するために、プロットにマーカーを追加します。

```python
# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```
