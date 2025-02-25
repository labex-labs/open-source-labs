# Configurar la representación gráfica

En este paso, configuraremos la representación gráfica para la representación gráfica de superficie 3D. Utilizaremos un objeto LightSource para personalizar la iluminación de relieve.

```python
# Configurar la representación gráfica
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# Para utilizar un modo de iluminación de relieve personalizado, anule la iluminación predeterminada y pase
# los colores rgb de la superficie iluminada calculados a partir de "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```
