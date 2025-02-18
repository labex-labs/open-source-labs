# Erstellen des Textes für das Textfeld

Wir werden einen String erstellen, der den Mittelwert (mean), Median und die Standardabweichung (standard deviation) unserer Daten enthält.

```python
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))
```
