# Ajustar los límites del gráfico

A continuación, ajustaremos los límites del gráfico de modo que la línea diagonal no tenga un ángulo de 45 grados cuando se vea en la pantalla. Esto creará un escenario en el que tendremos que rotar el texto con respecto a la línea, en lugar del sistema de coordenadas de la pantalla.

```python
# establecer límites para que no parezca tener un ángulo de 45 grados en la pantalla
ax.set_xlim([-10, 20])
```
