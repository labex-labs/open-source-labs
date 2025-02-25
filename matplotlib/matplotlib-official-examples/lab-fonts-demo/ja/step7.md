# 太字と斜体

調べる最後のフォントプロパティは、スタイルと太さオプションの組み合わせです。このプロパティを使用すると、グラフで使用するフォントのスタイルと太さを設定できます。

```python
# Show bold italic
font = FontProperties(style='italic', weight='bold', size='x-small')
fig.text(0.3, 0.1, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='medium')
fig.text(0.3, 0.2, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='x-large')
fig.text(0.3, 0.3, 'bold italic', fontproperties=font, **alignment)
```
