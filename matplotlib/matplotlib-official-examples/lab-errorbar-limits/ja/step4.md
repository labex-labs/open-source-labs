# 上限を追加する

エラーバーに上限を追加するには、`errorbar`関数の`uplims`パラメータを使用します。また、このプロットと前のプロットを区別するために、y値に0.5の定数値を追加します。

```python
# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
