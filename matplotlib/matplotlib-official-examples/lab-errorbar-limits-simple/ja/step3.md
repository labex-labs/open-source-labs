# 両方の制限付きのエラーバープロットを作成する（デフォルト）

このステップでは、上限と下限の両方があるエラーバープロットを作成します。これはデフォルトの動作です。

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```
