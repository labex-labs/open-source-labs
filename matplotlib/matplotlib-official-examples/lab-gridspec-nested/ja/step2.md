# グラフと外側のグリッドスペックの作成

次のステップは、グラフと外側のグリッドスペックを作成することです。この例では、1 行 2 列のグリッドスペックを作成します。

```python
fig = plt.figure()
gs0 = gridspec.GridSpec(1, 2, figure=fig)
```
