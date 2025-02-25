# Créez le premier ensemble de motifs de hachure

Nous allons créer le premier ensemble de motifs de hachure à l'aide de la liste suivante :

```python
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
```

Nous utiliserons ensuite une boucle pour créer un rectangle avec chaque motif de hachure et l'ajouter à un sous-graphique.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
