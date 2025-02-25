# Hinzufügen von Text zum Plot

Wir können Text zum Plot hinzufügen, indem wir die Funktion `ax.text()` verwenden. Diese Funktion nimmt drei Argumente entgegen: die x-Koordinate, die y-Koordinate und die Texteingabe. Wir können den Textstil mit den Argumenten `style`, `bbox` und `fontsize` anpassen.

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```
