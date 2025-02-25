# Загрузка глифа

Теперь мы загрузим глиф, букву 'A', из шрифта и выведем его ограничивающий прямоугольник с использованием атрибута `glyph.bbox`.

```python
code = coded['A']
glyph = font.load_char(code)
print(glyph.bbox)
```
