# 绘制路径长度决策边界

通过设置`response_method="decision_function"`，`DecisionBoundaryDisplay`的背景表示一个观测值的正态性度量。这样的分数由在随机树森林上平均的路径长度给出，而路径长度本身由隔离给定样本所需的叶节点深度（或等效地，分割次数）给出。

```python
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="decision_function",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("Path length decision boundary \nof IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["outliers", "inliers"], title="true class")
plt.colorbar(disp.ax_.collections[1])
plt.show()
```
