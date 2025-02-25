# 上限と下限のサブセットを持つエラーバープロットを作成する

このステップでは、上限と下限のサブセットを持つエラーバープロットを作成します。

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```
