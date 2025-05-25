# Obter Valores de Kerning

Podemos obter os valores de kerning entre dois glifos usando o método `font.get_kerning()`. Neste exemplo, obteremos o valor de kerning entre os glifos para 'A' e 'V' e os glifos para 'A' e 'T'.

```python
# kerning values for 'AV'
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# kerning value for 'AT'
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```
