# Zeige Schriftarten

Als nächstes werden wir die verschiedenen Schriftarten in Matplotlib anzeigen. Wir werden die `fig.text()`-Methode verwenden, um jede Schriftart anzuzeigen, wobei der Name der Schriftart als Text und die entsprechende Schriftart als Schlüsselwortargument verwendet wird.

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```
