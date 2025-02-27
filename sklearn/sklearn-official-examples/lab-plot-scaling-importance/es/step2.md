# Efecto de la reescalación en un modelo de k-vecinos más cercanos

Utilizaremos un subconjunto de dos características del conjunto de datos de vinos para entrenar un clasificador de k-vecinos más cercanos. Visualizaremos el límite de decisión del clasificador utilizando datos no escalados y escalados.

```python
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.neighbors import KNeighborsClassifier

X_plot = X[["proline", "hue"]]
X_plot_scaled = scaler.fit_transform(X_plot)
clf = KNeighborsClassifier(n_neighbors=20)

def fit_and_plot_model(X_plot, y, clf, ax):
    clf.fit(X_plot, y)
    disp = DecisionBoundaryDisplay.from_estimator(
        clf,
        X_plot,
        response_method="predict",
        alpha=0.5,
        ax=ax,
    )
    disp.ax_.scatter(X_plot["proline"], X_plot["hue"], c=y, s=20, edgecolor="k")
    disp.ax_.set_xlim((X_plot["proline"].min(), X_plot["proline"].max()))
    disp.ax_.set_ylim((X_plot["hue"].min(), X_plot["hue"].max()))
    return disp.ax_

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))

fit_and_plot_model(X_plot, y, clf, ax1)
ax1.set_title("KNN sin escalado")

fit_and_plot_model(X_plot_scaled, y, clf, ax2)
ax2.set_xlabel("proline escalado")
ax2.set_ylabel("hue escalado")
_ = ax2.set_title("KNN con escalado")
```
