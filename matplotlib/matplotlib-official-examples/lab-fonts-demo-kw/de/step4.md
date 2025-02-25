# Zeige Schriftvarianten

Als nächstes werden wir die verschiedenen Schriftvarianten in Matplotlib anzeigen. Wir werden die `fig.text()`-Methode verwenden, um jede Schriftvariante anzuzeigen, wobei der Variantenname als Text und die entsprechende Schriftvariante als Schlüsselwortargument verwendet wird.

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal','small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```
