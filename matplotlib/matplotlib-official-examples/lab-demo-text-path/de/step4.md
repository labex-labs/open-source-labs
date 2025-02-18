# Erstellen einer Offset-Box

Erstellen Sie eine Offset-Box mit `AuxTransformBox`, um das `PathClippedImagePatch`-Objekt hinzuzufügen. Verwenden Sie den folgenden Code, um die Offset-Box zu erstellen:

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
