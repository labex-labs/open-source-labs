# グラフとサブプロットの作成

`add_gridspec` メソッドを使って、2つのサブプロット付きのグラフを作成します。

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```
