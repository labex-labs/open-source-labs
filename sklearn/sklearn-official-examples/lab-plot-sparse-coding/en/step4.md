# Compute a Wavelet Dictionary

We will compute a wavelet dictionary and visualize it using Matplotlib.

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
    plt.title("Wavelet Dictionary (%s)" % ("fixed width" if i == 0 else "multiple widths"))
    plt.axis("off")
plt.show()
```
