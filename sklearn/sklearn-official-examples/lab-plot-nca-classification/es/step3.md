# Crear mapas de colores

Ahora crearemos mapas de colores para graficar los límites de decisión de clase. Usaremos colores claros para el fondo y colores en negrita para los colores de las clases.

```python
h = 0.05  # tamaño del paso en la malla

# Crear mapas de colores
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```
