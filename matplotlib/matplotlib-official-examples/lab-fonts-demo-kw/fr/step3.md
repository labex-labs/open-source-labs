# Afficher les styles de police

Maintenant, nous allons afficher les différents styles de police disponibles dans Matplotlib. Nous utiliserons la méthode `fig.text()` pour afficher chaque style de police, avec le nom du style comme texte et le style de police correspondant comme argument clé.

```python
fig.text(0.3, 0.9,'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```
