# Style 옵션

두 번째로 살펴볼 글꼴 속성은 style 옵션입니다. 이 속성을 사용하면 플롯에 사용되는 글꼴 스타일 (style) 을 설정할 수 있습니다.

```python
# Show style options
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9, 'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```
