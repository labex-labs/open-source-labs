# 创建 3D 体素图

现在我们使用`ax.voxels`函数创建 3D 体素图。我们将`x`、`y`、`z`和`sphere`作为参数传入。我们还使用之前定义的`colors`数组添加`facecolors`和`edgecolors`。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # 更亮
          linewidth=0.5)
```
