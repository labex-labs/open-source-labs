# Trainingspunkte plotten

Wir werden nun die Trainingspunkte auf der Entscheidungsfläche darstellen. Wir werden die `scatter()`-Methode verwenden, um die Trainingspunkte mit unterschiedlichen Farben für verschiedene Zielwerte zu plotten.

```python
for i, color in zip(clf.classes_, colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=color,
        label=iris.target_names[i],
        cmap=plt.cm.Paired,
        edgecolor="black",
        s=20,
    )
plt.title("Decision surface of multi-class SGD")
plt.axis("tight")
```
