# Créer une boîte de décalage (offset box)

Créez une boîte de décalage en utilisant `AuxTransformBox` pour ajouter l'objet `PathClippedImagePatch`. Utilisez le code suivant pour créer la boîte de décalage :

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
