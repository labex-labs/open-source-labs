# 上限のみのエラーバープロットを作成する

このステップでは、上限のみのエラーバープロットを作成します。

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```
