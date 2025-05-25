# Criando o Gráfico de Superfície 3D

Agora podemos criar o gráfico de superfície 3D. Começamos criando uma figura e adicionando um subplot com o argumento `projection='3d'`. Em seguida, usamos a função `plot_surface()` para plotar a superfície usando os dados que criamos no passo anterior.

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
