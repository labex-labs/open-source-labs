# 一方向にサブプロットを積み重ねる

垂直または水平に積み重ねた複数のサブプロットを作成するには、行数と列数を引数として`subplots()`関数に渡すことができます。返される`axs`オブジェクトは、作成された`Axes`のリストを含む 1 次元の numpy 配列です。

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```
