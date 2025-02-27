# Berechne ein Wellenlet-Wörterbuch

Wir werden ein Wellenlet-Wörterbuch berechnen und es mit Matplotlib visualisieren.

```python
# Compute a wavelet dictionary
D_fixed = ricker_matrix(width=width, resolution=resolution, n_components=n_components)
D_multi = np.r_[
    tuple(
        ricker_matrix(width=w, resolution=resolution, n_components=n_components // 5)
        for w in (10, 50, 100, 500, 1000)
    )
]

# Visualize the wavelet dictionary
plt.figure(figsize=(10, 5))
for i, D in enumerate((D_fixed, D_multi)):
    plt.subplot(1, 2, i + 1)
    plt.imshow(D, cmap=plt.cm.gray, interpolation="nearest")
    plt.title("Wellenlet-Wörterbuch (%s)" % ("fester Breite" if i == 0 else "mehrere Breiten"))
    plt.axis("off")
plt.show()
```
