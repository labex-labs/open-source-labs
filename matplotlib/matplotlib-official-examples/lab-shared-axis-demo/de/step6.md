# Entfernen von Strichmarkenbeschriftungen

Wir können die Strichmarkenbeschriftungen eines bestimmten Teilplots entfernen, indem wir die Sichtbarkeit der Beschriftungen mit der `ax.get_xticklabels()`-Methode ändern. In diesem Beispiel werden wir die Strichmarkenbeschriftungen auf der x-Achse des zweiten Teilplots entfernen.

```python
plt.tick_params('x', labelbottom=False)
```
