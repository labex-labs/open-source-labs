# 上限を追加する

エラーバーに上限を追加するには、`errorbar`関数の`uplims`パラメータを使用します。また、このプロットと前のプロットを区別するために、y 値に 0.5 の定数値を追加します。

```python
# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
