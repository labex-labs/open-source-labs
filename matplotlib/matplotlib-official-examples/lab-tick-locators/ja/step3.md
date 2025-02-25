# ヌルロケータの定義

ヌルロケータは、軸にメモリを配置しないロケータです。`ticker.NullLocator()` を使用してヌルロケータを定義できます。

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
