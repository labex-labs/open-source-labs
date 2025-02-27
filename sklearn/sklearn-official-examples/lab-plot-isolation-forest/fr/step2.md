# Visualiser l'ensemble de données

Nous pouvons visualiser les grappes résultantes pour voir à quoi ressemble l'ensemble de données.

```python
import matplotlib.pyplot as plt

scatter = plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
handles, labels = scatter.legend_elements()
plt.axis("square")
plt.legend(handles=handles, labels=["anomalies", "données normales"], title="classe réelle")
plt.title("Données normales gaussiennes avec \nanomalies distribuées uniformément")
plt.show()
```
