# 固定ロケータの定義

固定ロケータは、固定された位置にメモリを配置するロケータです。`ticker.FixedLocator()` を使用して固定ロケータを定義できます。

```python
setup(axs[2], title="FixedLocator([0, 1, 5])")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))
```
