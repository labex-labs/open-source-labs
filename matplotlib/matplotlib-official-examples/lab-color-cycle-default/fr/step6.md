# Personnalisez les sous-graphiques

Nous personnalisons les sous-graphiques en définissant la couleur d'arrière-plan des sous-graphiques inférieurs sur noir, en définissant les repères de l'axe x et en ajoutant un titre à chaque sous-graphique.

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'largeurs de ligne (pts) : {lwx:g}, {lwy:g}',
                       fontsize='medium')
```
