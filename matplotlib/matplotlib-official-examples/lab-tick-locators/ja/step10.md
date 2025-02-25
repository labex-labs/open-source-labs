# 対数ロケータの定義

対数ロケータは、対数スケール上で一定の間隔で目盛りを配置するロケータです。`ticker.LogLocator()` を使用して対数ロケータを定義できます。

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
