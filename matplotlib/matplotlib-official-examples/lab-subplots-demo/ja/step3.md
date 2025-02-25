# 二方向にサブプロットを積み重ねる

サブプロットのグリッドを作成するには、行数と列数を引数として`subplots()`関数に渡すことができます。返される`axs`オブジェクトは2次元のNumPy配列です。

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```
