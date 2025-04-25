# サーフェスプロットを作成する

このステップでは、作成した配列からの面の色を使ってサーフェスプロットを作成します。また、z 軸をカスタマイズします。

```python
# Create the surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)

# Customize the z axis
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(6))

# Show the plot
plt.show()
```
