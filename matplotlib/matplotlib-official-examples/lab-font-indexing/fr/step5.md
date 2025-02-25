# Obtenir les valeurs de kerning

Nous pouvons obtenir les valeurs de kerning entre deux glyphes en utilisant la méthode `font.get_kerning()`. Dans cet exemple, nous allons obtenir la valeur de kerning entre les glyphes pour 'A' et 'V' et les glyphes pour 'A' et 'T'.

```python
# kerning values for 'AV'
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# kerning value for 'AT'
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```
