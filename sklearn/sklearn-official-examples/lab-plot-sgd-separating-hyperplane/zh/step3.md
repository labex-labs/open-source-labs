# 绘制最大间隔分离超平面

最后，我们可以绘制使用随机梯度下降的支持向量机算法得到的最大间隔分离超平面。我们将使用`np.meshgrid`创建一个点网格，然后使用支持向量机模型的`decision_function`方法为网格上的每个点计算决策函数。然后，我们将使用`plt.contour`绘制决策边界，并使用`plt.scatter`绘制数据点。

```python
# 绘制直线、点以及到平面的最近向量
xx = np.linspace(-1, 5, 10)
yy = np.linspace(-1, 5, 10)

X1, X2 = np.meshgrid(xx, yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function([[x1, x2]])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ["dashed", "solid", "dashed"]
colors = "k"
plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolor="black", s=20)

plt.axis("tight")
plt.show()
```
