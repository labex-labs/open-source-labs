# プロットの作成

データが用意できたので、ワイヤーフレームプロットを作成できます。この例では、`plot_wireframe()`関数を使用してプロットを作成します。

```python
# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
