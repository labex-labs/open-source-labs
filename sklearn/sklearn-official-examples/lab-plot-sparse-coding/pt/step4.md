# Calcular um Dicionário de Ondas

Vamos calcular um dicionário de ondas e visualizá-lo usando Matplotlib.

```python
# Calcular um dicionário de ondas
D_fixed = ricker_matrix(width=width, resolution=resolution, n_components=n_components)
D_multi = np.r_[
    tuple(
        ricker_matrix(width=w, resolution=resolution, n_components=n_components // 5)
        for w in (10, 50, 100, 500, 1000)
    )
]

# Visualizar o dicionário de ondas
plt.figure(figsize=(10, 5))
for i, D in enumerate((D_fixed, D_multi)):
    plt.subplot(1, 2, i + 1)
    plt.imshow(D, cmap=plt.cm.gray, interpolation="nearest")
    plt.title("Dicionário de Ondas (%s)" % ("largura fixa" if i == 0 else "larguras múltiplas"))
    plt.axis("off")
plt.show()
```
