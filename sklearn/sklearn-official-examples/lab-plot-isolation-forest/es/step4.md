# Graficar el límite de decisión discreto

Usaremos la clase `DecisionBoundaryDisplay` para visualizar un límite de decisión discreto. El color de fondo representa si se predice que una muestra en esa área dada es un valor atípico o no. La gráfica de dispersión muestra las etiquetas reales.

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
