# Ajouter une flèche de texte pour indiquer la direction

Pour indiquer la direction des données, nous ajouterons une flèche de texte en utilisant la fonction `ax.text()` et le paramètre `bbox` avec le `boxstyle` défini sur "rarrow".

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```
