# グリフの読み込み

次に、フォントからグリフ（文字'A'）を読み込み、`glyph.bbox`属性を使ってそのバウンディングボックスを表示します。

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
