# Définir les limites de l'axe et enregistrer la figure

Nous définissons les limites x et y de l'axe et enregistrons la figure sous forme de chaîne de caractères binaire au format SVG à l'aide de `io.BytesIO()` et `plt.savefig()`.

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
