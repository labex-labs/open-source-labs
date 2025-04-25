# 3 次元プロットの作成

次に、`plt.figure()`と`fig.add_subplot()`関数を使って 3 次元プロットを作成します。また、`ax.plot_wireframe()`関数を使ってデータセットをワイヤーフレームとしてプロットします。

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
