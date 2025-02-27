# Effet de la mise à l'échelle sur la réduction de dimension par l'Analyse en Composantes Principales (PCA)

Nous utiliserons l'Analyse en Composantes Principales (PCA) pour réduire la dimension de l'ensemble de données sur le vin. Nous comparerons les composantes principales trouvées en utilisant la PCA sur des données non mises à l'échelle avec celles obtenues lorsqu'on utilise d'abord un StandardScaler pour mettre à l'échelle les données.

```python
import pandas as pd
from sklearn.decomposition import PCA

pca = PCA(n_components=2).fit(X_train)
scaled_pca = PCA(n_components=2).fit(scaled_X_train)
X_train_transformed = pca.transform(X_train)
X_train_std_transformed = scaled_pca.transform(scaled_X_train)

first_pca_component = pd.DataFrame(
    pca.components_[0], index=X.columns, columns=["without scaling"]
)
first_pca_component["with scaling"] = scaled_pca.components_[0]
first_pca_component.plot.bar(
    title="Weights of the first principal component", figsize=(6, 8)
)

_ = plt.tight_layout()

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

target_classes = range(0, 3)
colors = ("blue", "red", "green")
markers = ("^", "s", "o")

for target_class, color, marker in zip(target_classes, colors, markers):
    ax1.scatter(
        x=X_train_transformed[y_train == target_class, 0],
        y=X_train_transformed[y_train == target_class, 1],
        color=color,
        label=f"class {target_class}",
        alpha=0.5,
        marker=marker,
    )

    ax2.scatter(
        x=X_train_std_transformed[y_train == target_class, 0],
        y=X_train_std_transformed[y_train == target_class, 1],
        color=color,
        label=f"class {target_class}",
        alpha=0.5,
        marker=marker,
    )

ax1.set_title("Ensemble d'entraînement non mis à l'échelle après PCA")
ax2.set_title("Ensemble d'entraînement standardisé après PCA")

for ax in (ax1, ax2):
    ax.set_xlabel("1ère composante principale")
    ax.set_ylabel("2ème composante principale")
    ax.legend(loc="upper right")
    ax.grid()

_ = plt.tight_layout()
```
