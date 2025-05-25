# Criar um Gráfico Polar (Polar Plot)

Agora criaremos um gráfico polar usando a função `polar` de `matplotlib.pyplot`.

```python
ax = plt.subplot(2, 1, 2, projection='polar')

# Plot the data
for x, y in zip(xs, ys):
    plt.polar(x, y, 'ro')
```
