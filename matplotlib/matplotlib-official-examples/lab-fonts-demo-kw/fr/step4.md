# Afficher les variantes de police

Ensuite, nous allons afficher les différentes variantes de police disponibles dans Matplotlib. Nous utiliserons la méthode `fig.text()` pour afficher chaque variante de police, avec le nom de la variante comme texte et la variante de police correspondante comme argument clé.

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal','small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```
