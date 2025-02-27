# Visualisiere Entscheidungsgrenzen

Wir werden nun die Entscheidungsgrenzen von Entscheidungsbäumen visualisieren, die auf Paaren von Merkmalen des Iris-Datensatzes trainiert wurden.

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.inspection import DecisionBoundaryDisplay

# Parameter
n_classes = 3
plot_colors = "ryb"
plot_step = 0.02

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):
    # Wir nehmen nur die beiden entsprechenden Merkmale
    X = iris.data[:, pair]
    y = iris.target

    # Trainiere
    clf = DecisionTreeClassifier().fit(X, y)

    # Zeichne die Entscheidungsgrenze
    ax = plt.subplot(2, 3, pairidx + 1)
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=plt.cm.RdYlBu,
        response_method="predict",
        ax=ax,
        xlabel=iris.feature_names[pair[0]],
        ylabel=iris.feature_names[pair[1]],
    )

    # Zeichne die Trainingspunkte
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0],
            X[idx, 1],
            c=color,
            label=iris.target_names[i],
            cmap=plt.cm.RdYlBu,
            edgecolor="black",
            s=15,
        )

plt.suptitle("Entscheidungsfläche von Entscheidungsbäumen, die auf Paaren von Merkmalen trainiert wurden")
plt.legend(loc="lower right", borderpad=0, handletextpad=0)
_ = plt.axis("tight")
```
