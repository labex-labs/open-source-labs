# 创建三角剖分

第一步是使用给定的 x、y 和三角形数据创建一个三角剖分。然后我们将绘制该三角剖分。

```python
# 创建三角剖分。
x = np.asarray([0, 1, 2, 3, 0.5, 1.5, 2.5, 1, 2, 1.5])
y = np.asarray([0, 0, 0, 0, 1.0, 1.0, 1.0, 2, 2, 3.0])
triangles = [[0, 1, 4], [1, 2, 5], [2, 3, 6], [1, 5, 4], [2, 6, 5], [4, 5, 7],
             [5, 6, 8], [5, 8, 7], [7, 8, 9]]
triang = mtri.Triangulation(x, y, triangles)

# 绘制三角剖分。
plt.triplot(triang, 'ko-')
plt.title('Triangular grid')
plt.show()
```
