# Enregistrer la figure au format SVG

Nous enregistrons la figure dans un objet de fichier fictif à l'aide de la classe `BytesIO` et de la méthode `savefig`.

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```
