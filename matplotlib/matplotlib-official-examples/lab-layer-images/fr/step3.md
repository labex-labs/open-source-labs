# Définissez la plage et créez la première image

Définissez la plage et créez la première image en utilisant la fonction `imshow`.

```python
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8)) % 2  # damier
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)
```
