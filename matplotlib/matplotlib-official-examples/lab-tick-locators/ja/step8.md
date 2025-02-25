# 自動ロケータの定義

自動ロケータは、一定の間隔で自動的にメモリを配置するロケータです。`ticker.AutoLocator()` を使用して自動ロケータを定義できます。

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
