# Personalizar o sombreamento de colina (Hillshading)

Nesta etapa, personalizaremos o sombreamento de colina (hillshading) substituindo o sombreamento integrado e passando as cores RGB da superfície sombreada calculadas a partir de "shade".

```python
# Set up plot
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```
