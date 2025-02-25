# Zeige Schriftgrößen

Schließlich werden wir die verschiedenen Schriftgrößen in Matplotlib anzeigen. Wir werden die `fig.text()`-Methode verwenden, um jede Schriftgröße anzuzeigen, wobei der Größenname als Text und die entsprechende Schriftgröße als Schlüsselwortargument verwendet wird.

```python
fig.text(0.9, 0.9,'size', **alignment)
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```
