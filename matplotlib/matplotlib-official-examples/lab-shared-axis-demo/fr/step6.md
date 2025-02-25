# Supprimer les étiquettes d'échelonnement

Nous pouvons supprimer les étiquettes d'échelonnement d'un sous-graphique spécifique en modifiant la visibilité des étiquettes à l'aide de la méthode `ax.get_xticklabels()`. Dans cet exemple, nous allons supprimer les étiquettes d'échelonnement sur l'axe x du deuxième sous-graphique.

```python
plt.tick_params('x', labelbottom=False)
```
