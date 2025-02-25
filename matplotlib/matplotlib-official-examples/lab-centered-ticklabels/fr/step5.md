# Ajuster l'alignement des étiquettes des graduations mineures

Enfin, nous devons aligner les étiquettes des graduations mineures au centre entre les graduations majeures. Nous pouvons le faire à l'aide de la fonction `get_xticklabels()` et en définissant le paramètre `minor` sur `True` pour obtenir les étiquettes des graduations mineures. Nous pouvons ensuite parcourir les étiquettes et définir l'alignement horizontal sur `'center'`.

```python
# Ajuster l'alignement des étiquettes des graduations mineures
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```
