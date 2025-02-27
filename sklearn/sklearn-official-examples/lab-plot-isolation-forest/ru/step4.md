# Построение дискретной границы решения

Мы будем использовать класс `DecisionBoundaryDisplay` для визуализации дискретной границы решения. Цвет фона показывает, предсказывается ли образец в данной области как выброс или нет. Диаграмма рассеяния отображает истинные метки.

```python
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay

disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="predict",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("Binary decision boundary \nof IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["outliers", "inliers"], title="true class")
plt.show()
```
