# Hinzufügen von Text

In diesem Schritt fügen wir Text zum Diagramm hinzu, indem wir die `text()`-Funktion verwenden.

```python
tex = r'$\mathcal{R}\prod_{i=\alpha_{i+1}}^\infty a_i\sin(2 \pi f x_i)$'
ax.text(1, 1.6, tex, fontsize=20, va='bottom')
```
