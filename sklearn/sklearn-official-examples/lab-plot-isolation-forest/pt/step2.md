# Visualizar o Conjunto de Dados

Podemos visualizar os clusters resultantes para ver como o conjunto de dados se apresenta.

```python
import matplotlib.pyplot as plt

scatter = plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
handles, labels = scatter.legend_elements()
plt.axis("square")
plt.legend(handles=handles, labels=["outliers", "inliers"], title="classe verdadeira")
plt.title("Valores normais gaussianos com \noutliers distribuídos uniformemente")
plt.show()
```
