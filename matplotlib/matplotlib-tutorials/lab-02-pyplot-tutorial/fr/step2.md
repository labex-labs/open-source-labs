# Formater le style du graphique

Ensuite, personnalisons le style de notre graphique. Nous pouvons utiliser le troisième argument optionnel de la fonction `plot` pour spécifier la chaîne de formatage, qui indique la couleur et le type de ligne du graphique. Par exemple, traçons le même graphique en ligne avec des cercles rouges :

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

Explication :

- Nous utilisons la chaîne de formatage `'ro'` pour indiquer des cercles rouges pour le graphique.
- La fonction `axis` est utilisée pour définir la zone d'affichage des axes, en spécifiant la plage de valeurs pour l'axe x et l'axe y.
