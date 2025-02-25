# Obtener valores de empalme

Podemos obtener los valores de empalme entre dos glifos utilizando el método `font.get_kerning()`. En este ejemplo, obtendremos el valor de empalme entre los glifos para 'A' y 'V' y los glifos para 'A' y 'T'.

```python
# valores de empalme para 'AV'
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# valor de empalme para 'AT'
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```
