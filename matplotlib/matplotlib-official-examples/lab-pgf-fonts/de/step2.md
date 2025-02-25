# Setzen der Schriftfamilie

Wir werden die Schriftfamilie auf "serif" setzen, indem wir den Parameter `font.family` verwenden. Darüber hinaus werden wir den Parameter `font.serif` auf eine leere Liste setzen, um die standardmäßige LaTeX-Serifenschrift zu verwenden.

```python
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": [],
})
```
