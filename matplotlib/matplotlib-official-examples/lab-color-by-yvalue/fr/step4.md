# Création du graphique

Dans cette étape, nous allons créer le graphique en utilisant les tableaux masqués créés dans l'étape précédente. Nous allons tracer chaque tableau masqué séparément et utiliser une couleur différente pour chacun d'eux.

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```
