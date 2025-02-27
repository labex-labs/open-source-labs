# Effekt der Skalierung auf die PCA-Dimensionalitätreduzierung

Wir werden die Hauptkomponentenanalyse (PCA) verwenden, um die Dimensionalität des Weindatensatzes zu reduzieren. Wir werden die Hauptkomponenten, die mit PCA auf nicht skalierten Daten gefunden werden, mit denen vergleichen, die erhalten werden, wenn man zuerst die Daten mit StandardScaler skaliert.

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
    title="Gewichte der ersten Hauptkomponente", figsize=(6, 8)
)

_ = plt.tight_layout()

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

target_classes = range(0, 3)
colors = ("blau", "rot", "grün")
markierungen = ("^", "s", "o")

for target_class, color, marker in zip(target_classes, colors, markierungen):
    ax1.scatter(
        x=X_train_transformed[y_train == target_class, 0],
        y=X_train_transformed[y_train == target_class, 1],
        color=color,
        label=f"Klasse {target_class}",
        alpha=0.5,
        marker=marker,
    )

    ax2.scatter(
        x=X_train_std_transformed[y_train == target_class, 0],
        y=X_train_std_transformed[y_train == target_class, 1],
        color=color,
        label=f"Klasse {target_class}",
        alpha=0.5,
        marker=marker,
    )

ax1.set_title("Nicht skalierter Trainingsdatensatz nach PCA")
ax2.set_title("Standardisierter Trainingsdatensatz nach PCA")

for ax in (ax1, ax2):
    ax.set_xlabel("1. Hauptkomponente")
    ax.set_ylabel("2. Hauptkomponente")
    ax.legend(loc="oben rechts")
    ax.grid()

_ = plt.tight_layout()
```
