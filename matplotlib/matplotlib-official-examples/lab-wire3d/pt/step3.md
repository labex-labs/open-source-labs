# Criar o Gráfico

Agora que temos nossos dados, podemos criar o gráfico de wireframe. Neste exemplo, usaremos a função `plot_wireframe()` para criar o gráfico.

```python
# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
