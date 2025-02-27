# Mahalanobis-Distanzen konturieren

Wir werden die Konturen der Mahalanobis-Distanzen, die von beiden Methoden berechnet werden, darstellen. Beachten Sie, dass die robusten Mahalanobis-Distanzen auf der Grundlage von MCD die inneren schwarzen Punkte viel besser anpassen, während die auf MLE basierenden Distanzen stärker von den äußeren roten Punkten beeinflusst werden.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
# Zeichne den Datensatz
inlier_plot = ax.scatter(X[:, 0], X[:, 1], color="black", label="innerer Punkt")
outlier_plot = ax.scatter(
    X[:, 0][-n_outliers:], X[:, 1][-n_outliers:], color="red", label="äußerer Punkt"
)
ax.set_xlim(ax.get_xlim()[0], 10.0)
ax.set_title("Mahalanobis-Distanzen eines kontaminierten Datensatzes")

# Erstelle ein Gitter von Merkmal-1- und Merkmal-2-Werten
xx, yy = np.meshgrid(
    np.linspace(plt.xlim()[0], plt.xlim()[1], 100),
    np.linspace(plt.ylim()[0], plt.ylim()[1], 100),
)
zz = np.c_[xx.ravel(), yy.ravel()]
# Berechne die auf MLE basierenden Mahalanobis-Distanzen des Gitters
mahal_emp_cov = emp_cov.mahalanobis(zz)
mahal_emp_cov = mahal_emp_cov.reshape(xx.shape)
emp_cov_contour = plt.contour(
    xx, yy, np.sqrt(mahal_emp_cov), cmap=plt.cm.PuBu_r, linestyles="dashed"
)
# Berechne die auf MCD basierenden Mahalanobis-Distanzen
mahal_robust_cov = robust_cov.mahalanobis(zz)
mahal_robust_cov = mahal_robust_cov.reshape(xx.shape)
robust_contour = ax.contour(
    xx, yy, np.sqrt(mahal_robust_cov), cmap=plt.cm.YlOrBr_r, linestyles="dotted"
)

# Füge eine Legende hinzu
ax.legend(
    [
        emp_cov_contour.collections[1],
        robust_contour.collections[1],
        inlier_plot,
        outlier_plot,
    ],
    ["MLE-Dist", "MCD-Dist", "innerer Punkt", "äußerer Punkt"],
    loc="upper right",
    borderaxespad=0,
)

plt.show()
```
