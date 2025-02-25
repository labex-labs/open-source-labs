# Zeige Schriftgewichte

Jetzt werden wir die verschiedenen Schriftgewichte in Matplotlib anzeigen. Wir werden die `fig.text()`-Methode verwenden, um jedes Schriftgewicht anzuzeigen, wobei der Gewichtsname als Text und das entsprechende Schriftgewicht als Schlüsselwortargument verwendet wird.

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```
