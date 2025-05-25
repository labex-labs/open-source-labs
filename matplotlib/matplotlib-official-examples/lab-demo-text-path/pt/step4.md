# Criar uma Caixa de Deslocamento (Offset Box)

Crie uma caixa de deslocamento (offset box) usando AuxTransformBox para adicionar o objeto PathClippedImagePatch. Use o seguinte código para criar a caixa de deslocamento:

```python
offsetbox = AuxTransformBox(IdentityTransform())
offsetbox.add_artist(p)
```
