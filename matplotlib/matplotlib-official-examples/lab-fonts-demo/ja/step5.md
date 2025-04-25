# 太さオプション

4 番目に調べるフォントプロパティは、太さオプションです。このプロパティを使用すると、グラフで使用するフォントの太さを設定できます。

```python
# Show weight options
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```
