# Den Plot formatieren

Um unseren Plot lesbarer zu gestalten, können wir ihn mit den Formatierungsfunktionen von Matplotlib formatieren. In diesem Beispiel werden wir die y-Achsenbeschriftungen formatieren, um die Werte in Millionen anzuzeigen.

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```
