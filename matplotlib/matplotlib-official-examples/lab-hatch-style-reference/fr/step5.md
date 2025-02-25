# Créez le second ensemble de motifs de hachure

Nous allons créer le second ensemble de motifs de hachure en répétant chaque motif deux fois pour augmenter la densité. Nous utiliserons la liste suivante :

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

Nous utiliserons la même boucle que précédemment pour créer les rectangles.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
