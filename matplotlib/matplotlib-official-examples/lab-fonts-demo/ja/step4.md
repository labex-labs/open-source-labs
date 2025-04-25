# バリアントオプション

3 番目に調べるフォントプロパティは、バリアントオプションです。このプロパティを使用すると、グラフで使用するフォントのバリアントを設定できます。

```python
# Show variant options
variants = ['normal','small-caps']
fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
for k, variant in enumerate(variants):
    font = FontProperties()
    font.set_family('serif')
    font.set_variant(variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)
```
