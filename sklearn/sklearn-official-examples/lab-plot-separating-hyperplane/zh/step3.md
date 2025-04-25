# 绘制最大间隔分离超平面

为了绘制最大间隔分离超平面，我们将使用 scikit-learn 中的`DecisionBoundaryDisplay.from_estimator()`函数。此函数绘制 SVM 分类器的决策函数和支持向量。我们还将把支持向量绘制为没有填充、只有黑色边缘的圆圈。

```python
from sklearn.inspection import DecisionBoundaryDisplay

# 绘制决策函数和支持向量
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
```
