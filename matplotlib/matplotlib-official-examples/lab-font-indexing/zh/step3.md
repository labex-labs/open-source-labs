# 获取字符编码和字形

我们将获取字体中的字符编码及其对应的字形，并将它们存储在两个字典 `coded` 和 `glyphd` 中。

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
