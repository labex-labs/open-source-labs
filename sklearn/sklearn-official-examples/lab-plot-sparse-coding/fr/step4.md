# Calculer un dictionnaire d'ondelettes

Nous allons calculer un dictionnaire d'ondelettes et le visualiser à l'aide de Matplotlib.

```python
# Calculer un dictionnaire d'ondelettes
D_fixed = ricker_matrix(width=width, resolution=resolution, n_components=n_components)
D_multi = np.r_[
    tuple(
        ricker_matrix(width=w, resolution=resolution, n_components=n_components // 5)
        for w in (10, 50, 100, 500, 1000)
    )
]

# Visualiser le dictionnaire d'ondelettes
plt.figure(figsize=(10, 5))
for i, D in enumerate((D_fixed, D_multi)):
    plt.subplot(1, 2, i + 1)
    plt.imshow(D, cmap=plt.cm.gray, interpolation="nearest")
    plt.title("Dictionnaire d'ondelettes (%s)" % ("largeur fixe" si i == 0 else "plusieurs largeurs"))
    plt.axis("off")
plt.show()
```
