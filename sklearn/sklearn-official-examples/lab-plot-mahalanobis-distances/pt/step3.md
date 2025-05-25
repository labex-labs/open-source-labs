# Plotar Contornos das Distâncias de Mahalanobis

Plotaremos os contornos das distâncias de Mahalanobis calculadas por ambos os métodos. Note-se que as distâncias de Mahalanobis robustas baseadas em MCD ajustam-se muito melhor aos pontos internos pretos, enquanto as distâncias baseadas em MLE são mais influenciadas pelos pontos discrepantes vermelhos.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
# Plotar o conjunto de dados
inlier_plot = ax.scatter(X[:, 0], X[:, 1], color="black", label="inliers")
outlier_plot = ax.scatter(
    X[:, 0][-n_outliers:], X[:, 1][-n_outliers:], color="red", label="outliers"
)
ax.set_xlim(ax.get_xlim()[0], 10.0)
ax.set_title("Distâncias de Mahalanobis de um conjunto de dados contaminado")

# Criar malha de valores das características 1 e 2
xx, yy = np.meshgrid(
    np.linspace(plt.xlim()[0], plt.xlim()[1], 100),
    np.linspace(plt.ylim()[0], plt.ylim()[1], 100),
)
zz = np.c_[xx.ravel(), yy.ravel()]
# Calcular as distâncias de Mahalanobis baseadas em MLE da malha
mahal_emp_cov = emp_cov.mahalanobis(zz)
mahal_emp_cov = mahal_emp_cov.reshape(xx.shape)
emp_cov_contour = plt.contour(
    xx, yy, np.sqrt(mahal_emp_cov), cmap=plt.cm.PuBu_r, linestyles="dashed"
)
# Calcular as distâncias de Mahalanobis baseadas em MCD
mahal_robust_cov = robust_cov.mahalanobis(zz)
mahal_robust_cov = mahal_robust_cov.reshape(xx.shape)
robust_contour = ax.contour(
    xx, yy, np.sqrt(mahal_robust_cov), cmap=plt.cm.YlOrBr_r, linestyles="dotted"
)

# Adicionar legenda
ax.legend(
    [
        emp_cov_contour.collections[1],
        robust_contour.collections[1],
        inlier_plot,
        outlier_plot,
    ],
    ["Dist MLE", "Dist MCD", "inliers", "outliers"],
    loc="upper right",
    borderaxespad=0,
)

plt.show()
```
