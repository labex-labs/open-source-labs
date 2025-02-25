# Fettdruck und Kursivschrift

Die letzte Schriftart-Eigenschaft, die wir untersuchen werden, ist eine Kombination der Stil- und Gewicht-Optionen. Mit dieser Eigenschaft kannst du den Schriftstil und das Schriftgewicht festlegen, die in deinem Diagramm verwendet werden.

```python
# Zeige Fettdruck und Kursivschrift
font = FontProperties(style='italic', weight='bold', size='x-small')
fig.text(0.3, 0.1, 'Fettdruck und Kursivschrift', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='medium')
fig.text(0.3, 0.2, 'Fettdruck und Kursivschrift', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='x-large')
fig.text(0.3, 0.3, 'Fettdruck und Kursivschrift', fontproperties=font, **alignment)
```
