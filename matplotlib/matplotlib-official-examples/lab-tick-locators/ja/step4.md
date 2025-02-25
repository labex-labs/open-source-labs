# 複数ロケータの定義

複数ロケータは、一定の間隔でメモリを配置するロケータです。`ticker.MultipleLocator()` を使用して複数ロケータを定義できます。

```python
setup(axs[1], title="MultipleLocator(0.5, offset=0.2)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5, offset=0.2))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
```
