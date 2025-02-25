# グラフと外側のグリッドを作成する

次に、`add_gridspec` 関数を使用してグラフと外側のグリッドを作成します。サブプロット間に余白をなくした 4x4 のグリッドを作成します。

```python
fig = plt.figure(figsize=(8, 8))
outer_grid = fig.add_gridspec(4, 4, wspace=0, hspace=0)
```
