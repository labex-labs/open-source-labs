# 加载一个字形

现在我们将从字体中加载一个字形，即字母 'A'，并使用 `glyph.bbox` 属性打印其边界框。

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
