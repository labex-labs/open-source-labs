# 문자 코드 및 글리프 가져오기

글꼴에서 문자 코드와 해당 글리프를 가져와 `coded` 및 `glyphd` 두 개의 딕셔너리에 저장합니다.

```python
codes = font.get_charmap().items()

coded = {}
glyphd = {}
for ccode, glyphind in codes:
    name = font.get_glyph_name(glyphind)
    coded[name] = ccode
    glyphd[name] = glyphind
```
