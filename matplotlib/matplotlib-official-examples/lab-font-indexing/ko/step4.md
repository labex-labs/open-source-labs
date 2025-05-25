# 글리프 로드

이제 글꼴에서 문자 'A' 글리프를 로드하고 `glyph.bbox` 속성을 사용하여 경계 상자 (bounding box) 를 출력합니다.

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
