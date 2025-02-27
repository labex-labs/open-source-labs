# Calcular un diccionario de ondas

Calculemos un diccionario de ondas y visualicémoslo utilizando Matplotlib.

```python
# Calcular un diccionario de ondas
D_fixed = ricker_matrix(width=width, resolution=resolution, n_components=n_components)
D_multi = np.r_[
    tuple(
        ricker_matrix(width=w, resolution=resolution, n_components=n_components // 5)
        for w in (10, 50, 100, 500, 1000)
    )
]

# Visualizar el diccionario de ondas
plt.figure(figsize=(10, 5))
for i, D in enumerate((D_fixed, D_multi)):
    plt.subplot(1, 2, i + 1)
    plt.imshow(D, cmap=plt.cm.gray, interpolation="nearest")
    plt.title("Diccionario de ondas (%s)" % ("ancho fijo" si i == 0 else "varios anchos"))
    plt.axis("off")
plt.show()
```
