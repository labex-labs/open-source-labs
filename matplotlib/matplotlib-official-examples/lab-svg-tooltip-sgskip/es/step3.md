# Guardar la figura como SVG

Guardamos la figura en un objeto de archivo ficticio usando la clase `BytesIO` y el método `savefig`.

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```
