# Mostrar la imagen

Ahora podemos mostrar la imagen utilizando el método `imshow` de Matplotlib. También desactivaremos los ejes para que solo veamos la imagen.

```python
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')
```
