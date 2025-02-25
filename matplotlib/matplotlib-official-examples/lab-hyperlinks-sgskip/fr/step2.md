# Créer un graphique de dispersion avec des liens hypertexte

Dans cette étape, nous allons créer un graphique de dispersion et ajouter des liens hypertexte aux marqueurs. Voici le code pour créer le graphique de dispersion :

```python
fig = plt.figure()
s = plt.scatter([1, 2, 3], [4, 5, 6])
```

Pour ajouter des liens hypertexte, nous devons utiliser la méthode `set_urls()` de l'objet graphique de dispersion. Cette méthode prend une liste d'URLs en argument. Voici le code mis à jour :

```python
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
```

Les deux premiers marqueurs auront respectivement des liens hypertexte vers `https://www.bbc.com/news` et `https://www.google.com/`. Le troisième marqueur n'aura pas de lien hypertexte. Enfin, nous pouvons enregistrer le graphique sous forme de fichier SVG en utilisant `fig.savefig()` :

```python
fig.savefig('scatter.svg')
```
