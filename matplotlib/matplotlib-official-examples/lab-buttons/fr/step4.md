# Créez les boutons `Next` et `Previous`

Maintenant, nous allons créer les boutons `Next` et `Previous` à l'aide de la fonction `add_axes` de `matplotlib.pyplot`, et assigner les fonctions de rappel que nous avons créées précédemment à ces boutons en utilisant `on_clicked`.

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
