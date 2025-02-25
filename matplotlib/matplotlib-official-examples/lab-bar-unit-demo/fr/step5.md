# Créez le diagramme en barres

L'étape suivante est de créer le diagramme en barres. Nous allons utiliser la fonction `bar()` pour créer le graphique. Nous allons créer deux ensembles de barres, l'une pour le thé et l'autre pour le café. Nous ajouterons également des barres d'erreur au graphique.

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```
