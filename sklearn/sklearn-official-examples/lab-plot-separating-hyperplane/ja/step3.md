# 最大マージン分離超平面をプロットする

最大マージン分離超平面をプロットするには、scikit-learn の `DecisionBoundaryDisplay.from_estimator()` 関数を使います。この関数は、SVM 分類器の決定関数とサポートベクトルをプロットします。また、サポートベクトルを塗りつぶさない黒い枠の円としてプロットします。

```python
from sklearn.inspection import DecisionBoundaryDisplay

# plot the decision function and support vectors
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
