# Tracer les points d'entraînement

Nous allons maintenant tracer les points d'entraînement sur la surface de décision. Nous utiliserons la méthode scatter() pour tracer les points d'entraînement avec des couleurs différentes pour les différentes valeurs cibles.

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
