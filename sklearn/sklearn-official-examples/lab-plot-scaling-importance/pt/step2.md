# Efeito da Rescala em um Modelo k-vizinhos

Usaremos um subconjunto de dois recursos do conjunto de dados de vinho para treinar um classificador K-vizinhos mais próximos. Visualizaremos o limite de decisão do classificador usando dados não escalonados e escalonados.

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
ax1.set_title("KNN sem escala")

fit_and_plot_model(X_plot_scaled, y, clf, ax2)
ax2.set_xlabel("prolina escalonada")
ax2.set_ylabel("tom escalonado")
_ = ax2.set_title("KNN com escala")
```
