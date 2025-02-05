# 创建掩码风羽图

我们还可以通过使用掩码数组来创建掩码风羽图。在这种情况下，我们将把一个向量的值更改为一个无效值并对其进行掩码处理。

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # 当进行掩码处理时不应绘制的无效值
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```
