# 線形ロケータの定義

線形ロケータは、線形スケール上で一定の間隔でメモリを配置するロケータです。`ticker.LinearLocator()` を使用して線形ロケータを定義できます。

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
