# MaxNロケータの定義

MaxNロケータは、軸上に最大数の目盛りを配置するロケータです。`ticker.MaxNLocator()` を使用してMaxNロケータを定義できます。

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
