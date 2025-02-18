# Créer une boîte de décalage ancrée (anchored offset box)

Créez une boîte de décalage ancrée en utilisant `AnnotationBbox` pour ajouter la boîte de décalage et définir sa position. Utilisez le code suivant pour créer la boîte de décalage ancrée :

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```
