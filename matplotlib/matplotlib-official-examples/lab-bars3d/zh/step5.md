# 自定义坐标轴

现在我们将自定义3D图形的坐标轴。我们将分别使用 `set_xlabel()`、`set_ylabel()` 和 `set_zlabel()` 方法来设置x、y和z轴的标签。我们还将使用 `set_yticks()` 方法来设置y轴上的刻度。

```python
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_yticks(yticks)
```
