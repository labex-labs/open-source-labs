# 例としてのグラフ用のサブプロットを作成する

例としてのグラフを表示するために、3×3 のサブプロットのグリッドを作成します。

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
