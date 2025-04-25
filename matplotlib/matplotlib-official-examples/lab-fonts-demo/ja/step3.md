# スタイルオプション

2 番目に調べるフォントプロパティは、スタイルオプションです。このプロパティを使用すると、グラフで使用するフォントスタイルを設定できます。

```python
# Show style options
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9,'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```
