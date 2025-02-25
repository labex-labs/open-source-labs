# Definir la extensión y crear la primera imagen

Define la extensión y crea la primera imagen utilizando la función `imshow`.

```python
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8)) % 2  # tablero de ajedrez
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)
```
