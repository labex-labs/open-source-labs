# Graficar los puntos de entrenamiento

Ahora graficaremos los puntos de entrenamiento en la superficie de decisión. Usaremos el método scatter() para graficar los puntos de entrenamiento con diferentes colores para diferentes valores objetivo.

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
