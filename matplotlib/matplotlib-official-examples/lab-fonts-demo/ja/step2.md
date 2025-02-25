# フォントファミリのオプション

最初に調べるフォントプロパティは、フォントファミリのオプションです。このプロパティを使用すると、グラフで使用するフォントファミリを設定できます。

```python
# Show family options
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```
