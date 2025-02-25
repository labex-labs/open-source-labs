# Créez le troisième ensemble de motifs de hachure

Nous allons créer le troisième ensemble de motifs de hachure en combinant deux motifs pour en créer un nouveau. Nous utiliserons la liste suivante :

```python
hatches = ['/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-']
```

Nous utiliserons la même boucle que précédemment pour créer les rectangles.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
