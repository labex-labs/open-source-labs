# Création du texte pour la boîte de texte

Nous allons créer une chaîne de caractères contenant la moyenne, la médiane et l'écart-type de nos données.

```python
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))
```
