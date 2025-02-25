# 上限と下限の両方があるエラーバープロットを作成する

このステップでは、上限と下限の両方があるエラーバープロットを作成します。

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```
