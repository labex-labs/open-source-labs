# 3D ワイヤーフレームプロットの作成

2 番目のサブプロット用に 3D ワイヤーフレームプロットを作成します。このプロット用のデータを作成するために、mpl_toolkits.mplot3d.axes3d の `get_test_data` 関数を使用します。

```python
# Create data for the 3D wireframe plot
X, Y, Z = Axes3D.get_test_data(0.05)

# Plot the 3D wireframe plot
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
