# ネ字情報の取得

`font.get_kerning()`メソッドを使って、2 つのグリフ間のネ字情報を取得することができます。この例では、'A'と'V'のグリフ間、および'A'と'T'のグリフ間のネ字情報を取得します。

```python
# 'AV'のネ字情報
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# 'AT'のネ字情報
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```
