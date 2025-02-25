# Création de segments de ligne

Nous allons créer un ensemble de segments de ligne afin de pouvoir les colorer individuellement. Nous utiliserons la fonction `concatenate` de numpy pour concaténer deux tableaux `points[:-1]` et `points[1:]` le long du deuxième axe. Nous allons ensuite redimensionner le tableau résultant en un tableau N x 1 x 2 afin de pouvoir empiler facilement les points pour obtenir les segments. Le tableau de segments pour la collecte de lignes doit être de forme (numlines) x (points par ligne) x 2 (pour x et y).

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```
