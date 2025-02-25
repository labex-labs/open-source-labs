# Crear un diagrama de dispersión

Ahora crearemos un diagrama de dispersión usando la función `plot` de `matplotlib.pyplot`.

```python
fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

# Plot the data
for x, y in zip(xs, ys):
    plt.plot(x, y, 'ro')
```
