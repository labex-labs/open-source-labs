# 文字コードとグリフの取得

フォント内の文字コードと対応するグリフを取得し、それらを2つの辞書`coded`と`glyphd`に格納します。

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
