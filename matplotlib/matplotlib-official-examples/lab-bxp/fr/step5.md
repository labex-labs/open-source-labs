# Basculer l'affichage des différents éléments

Nous pouvons basculer l'affichage des différents éléments du diagramme en boîte en utilisant divers paramètres dans la fonction `bxp()`. Dans cet exemple, nous montrons comment afficher ou masquer la moyenne, la boîte, les bouchons, les encoches et les points aberrants.

```python
# Basculer l'affichage des différents éléments
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```
