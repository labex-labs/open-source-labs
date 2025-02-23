# Gráfico normal junto a una imagen

Al crear un gráfico de imagen con una relación de aspecto fija de datos y el valor predeterminado `adjustable="box"` junto a un gráfico normal, los ejes tendrían una altura desigual. `set_box_aspect()` ofrece una solución fácil a esto al permitir que los ejes del gráfico normal usen las dimensiones de la imagen como relación de aspecto del contenedor. Este ejemplo también muestra que el _diseño restringido_ interactúa perfectamente con una relación de aspecto fija del contenedor.

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```
