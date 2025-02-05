# 获取字距调整值

我们可以通过使用 `font.get_kerning()` 方法来获取两个字形之间的字距调整值。在这个例子中，我们将获取字母 'A' 和 'V' 的字形之间以及字母 'A' 和 'T' 的字形之间的字距调整值。

```python
# 'AV' 的字距调整值
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_DEFAULT))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNFITTED))
print('AV', font.get_kerning(glyphd['A'], glyphd['V'], KERNING_UNSCALED))

# 'AT' 的字距调整值
print('AT', font.get_kerning(glyphd['A'], glyphd['T'], KERNING_UNSCALED))
```
