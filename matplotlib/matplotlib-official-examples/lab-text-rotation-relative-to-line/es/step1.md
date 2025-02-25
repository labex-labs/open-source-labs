# Trazar una línea diagonal

En primer lugar, trazaremos una línea diagonal a un ángulo de 45 grados utilizando la función `plot()` de Matplotlib.

```python
fig, ax = plt.subplots()

# Trazar línea diagonal (45 grados)
h = ax.plot(range(0, 10), range(0, 10))
```
