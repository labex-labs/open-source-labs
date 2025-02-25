# Créer des axes insérés

Dans cette étape, nous créons deux axes insérés à l'intérieur des axes principaux du graphique à l'aide de `fig.add_axes`. L'un affichera un histogramme des données, et l'autre affichera la réponse impulsionnelle.

```python
# Create right inset axes
right_inset_ax = fig.add_axes([.65,.6,.2,.2], facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Probabilité', xticks=[], yticks=[])

# Create left inset axes
left_inset_ax = fig.add_axes([.2,.6,.2,.2], facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Réponse impulsionnelle', xlim=(0,.2), xticks=[], yticks=[])
```
