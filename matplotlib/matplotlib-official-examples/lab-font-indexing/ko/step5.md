# 커닝 값 가져오기

`font.get_kerning()` 메서드를 사용하여 두 글리프 사이의 커닝 값 (kerning values) 을 가져올 수 있습니다. 이 예제에서는 'A'와 'V' 글리프 사이의 커닝 값과 'A'와 'T' 글리프 사이의 커닝 값을 가져옵니다.

```python
# kerning values for 'AV'
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# kerning value for 'AT'
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```
