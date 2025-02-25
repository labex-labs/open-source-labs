# インデックスロケータの定義

インデックスロケータは、インデックススケール上で一定の間隔でメモリを配置するロケータです。`ticker.IndexLocator()` を使用してインデックスロケータを定義できます。

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
