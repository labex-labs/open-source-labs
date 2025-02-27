# Effet de la mise à l'échelle sur un modèle K-plus-proches-voisins

Nous utiliserons un sous-ensemble de deux fonctionnalités de l'ensemble de données sur le vin pour entraîner un classifieur K-plus-proches-voisins. Nous visualiserons la frontière de décision du classifieur en utilisant des données non mises à l'échelle et mises à l'échelle.

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
ax1.set_title("KNN sans mise à l'échelle")

fit_and_plot_model(X_plot_scaled, y, clf, ax2)
ax2.set_xlabel("proline mis à l'échelle")
ax2.set_ylabel("teinte mise à l'échelle")
_ = ax2.set_title("KNN avec mise à l'échelle")
```
