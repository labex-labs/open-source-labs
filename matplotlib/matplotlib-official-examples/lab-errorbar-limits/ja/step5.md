# 下限を追加する

エラーバーに下限を追加するには、`errorbar`関数の`lolims`パラメータを使用します。また、このプロットと前のプロットを区別するために、y値に1.0の定数値を追加します。

```python
# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```
