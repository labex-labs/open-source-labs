# Criar um Gráfico de Dispersão (Scatter Plot)

Agora criaremos um gráfico de dispersão usando a função `plot` de `matplotlib.pyplot`.

```python
fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

# Plot the data
for x, y in zip(xs, ys):
    plt.plot(x, y, 'ro')
```
