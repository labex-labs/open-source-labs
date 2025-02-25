# Créer des sous-graphiques

Nous créons trois sous-graphiques à l'aide de la fonction `subplots` dans Matplotlib. Nous définissons le paramètre `sharex` sur `True` pour vous assurer que les sous-graphiques partagent un axe x commun. Nous supprimons également l'espace vertical entre les sous-graphiques à l'aide de la fonction `subplots_adjust`.

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```
