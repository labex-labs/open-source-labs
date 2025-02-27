# Visualisiere den Datensatz

Wir können die resultierenden Cluster visualisieren, um zu sehen, wie der Datensatz aussieht.

```python
import matplotlib.pyplot as plt

scatter = plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
handles, labels = scatter.legend_elements()
plt.axis("square")
plt.legend(handles=handles, labels=["Ausreißer", "Innerpunkte"], title="wahre Klasse")
plt.title("Gaußsche Innerpunkte mit \ngleichmäßig verteilten Ausreißern")
plt.show()
```
