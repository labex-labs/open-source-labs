# Построение границы решения по длине пути

Задавая `response_method="decision_function"`, фон `DecisionBoundaryDisplay` представляет собой меру нормальности наблюдения. Такая оценка определяется средней длиной пути в лесу случайных деревьев, которая в свою очередь определяется глубиной листа (или эквивалентно количеством разбиений), необходимым для изоляции данного образца.

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
