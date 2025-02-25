# Personalizar la iluminación de relieve

En este paso, personalizaremos la iluminación de relieve anulando la iluminación predeterminada y pasando los colores RGB de la superficie iluminada calculados a partir de "shade".

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
