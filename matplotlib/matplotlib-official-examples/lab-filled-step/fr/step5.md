# Configurez les cycles de style

Nous allons configurer des cycles de style pour les histogrammes en utilisant `cycler`. Nous allons créer trois cycles de style : l'un pour la couleur de fond, l'un pour l'étiquette et l'un pour le motif de hachure.

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'ensemble {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```
