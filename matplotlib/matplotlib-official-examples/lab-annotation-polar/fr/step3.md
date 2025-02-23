# Ajouter une annotation

Nous pouvons ajouter une annotation au graphique polaire en spécifiant l'emplacement de l'annotation. Dans ce cas, nous choisissons un point spécifique sur le graphique et nous l'annotons.

```python
ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('une annotation polaire',
            xy=(thistheta, thisr),  # theta, rayon
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
```
