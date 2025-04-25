# サブプロットの作成

`subplots()`関数を使って、2x3 のサブプロットのグリッドを作成します。

```python
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
```
