# Plotar uma linha diagonal

Primeiramente, plotaremos uma linha diagonal em um ângulo de 45 graus usando a função `plot()` do Matplotlib.

```python
fig, ax = plt.subplots()

# Plot diagonal line (45 degrees)
h = ax.plot(range(0, 10), range(0, 10))
```
