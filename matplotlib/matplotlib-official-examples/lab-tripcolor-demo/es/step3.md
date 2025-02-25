# Crear un gráfico de tripcolor

Ahora, crearemos un gráfico de tripcolor utilizando la función `tripcolor()`. Crearemos dos gráficos utilizando diferentes métodos de sombreado.

```python
# Gráfico con sombreado plano
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor de la triangulación de Delaunay, sombreado plano')

# Gráfico con sombreado Gouraud
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
tpc = ax2.tripcolor(triang, z, shading='gouraud')
fig2.colorbar(tpc)
ax2.set_title('tripcolor de la triangulación de Delaunay, sombreado Gouraud')
```
