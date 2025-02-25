# Holt Kerning-Werte

Wir können die Kerning-Werte zwischen zwei Glyphen mit der Methode `font.get_kerning()` abrufen. In diesem Beispiel werden wir den Kerning-Wert zwischen den Glyphen für 'A' und 'V' und den Glyphen für 'A' und 'T' abrufen.

```python
# kerning values for 'AV'
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# kerning value for 'AT'
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```
