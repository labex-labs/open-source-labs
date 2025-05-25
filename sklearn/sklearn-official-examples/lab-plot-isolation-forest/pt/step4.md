# Plotar a Fronteira de Decisão Discreta

Usaremos a classe `DecisionBoundaryDisplay` para visualizar uma fronteira de decisão discreta. A cor de fundo representa se uma amostra nessa área específica é prevista como um outlier ou não. O gráfico de dispersão exibe as etiquetas verdadeiras.

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
disp.ax_.set_title("Fronteira de decisão binária \ndo IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["outliers", "inliers"], title="classe verdadeira")
plt.show()
```
