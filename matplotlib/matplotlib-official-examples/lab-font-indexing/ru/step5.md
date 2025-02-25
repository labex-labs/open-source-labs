# Получение значений кернинга

Мы можем получить значения кернинга между двумя глифами, используя метод `font.get_kerning()`. В этом примере мы получим значение кернинга между глифами для 'A' и 'V' и между глифами для 'A' и 'T'.

```python
# kerning values for 'AV'
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# kerning value for 'AT'
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```
