# Criar um Gráfico 3D

Em seguida, criaremos um gráfico 3D usando as funções `plt.figure()` e `fig.add_subplot()`. Também usaremos a função `ax.plot_wireframe()` para plotar o conjunto de dados como um wireframe.

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
