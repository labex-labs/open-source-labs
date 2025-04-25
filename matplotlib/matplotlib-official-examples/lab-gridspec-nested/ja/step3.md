# 内側のグリッドスペックの作成

次に、内側のグリッドスペックを作成します。外側のグリッドスペックのサブプロットとなる 3 行 3 列のグリッドスペックを作成するために、`GridSpecFromSubplotSpec`メソッドを使用します。

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```
