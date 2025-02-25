# Crear un diagrama de contorno simple con etiquetas

Ahora que tenemos nuestros datos, podemos crear un diagrama de contorno simple con etiquetas usando los colores predeterminados.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
