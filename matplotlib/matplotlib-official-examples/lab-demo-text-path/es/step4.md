# Crear una caja de desplazamiento (offset box)

Crea una caja de desplazamiento utilizando `AuxTransformBox` para agregar el objeto `PathClippedImagePatch`. Utiliza el siguiente código para crear la caja de desplazamiento:

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
