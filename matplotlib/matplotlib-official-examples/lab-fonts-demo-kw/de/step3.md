# Zeige Schriftstile

Jetzt werden wir die verschiedenen Schriftstile in Matplotlib anzeigen. Wir werden die `fig.text()`-Methode verwenden, um jeden Schriftstil anzuzeigen, wobei der Stilname als Text und der entsprechende Schriftstil als Schlüsselwortargument verwendet wird.

```python
fig.text(0.3, 0.9,'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```
