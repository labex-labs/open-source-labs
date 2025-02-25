# Establecer límites del eje y guardar la figura

Establecemos los límites x e y para el eje y guardamos la figura como una cadena de bytes en formato SVG utilizando `io.BytesIO()` y `plt.savefig()`.

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
