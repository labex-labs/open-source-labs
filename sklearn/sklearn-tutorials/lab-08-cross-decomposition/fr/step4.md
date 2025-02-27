# PLSCanonical

#### Ajustez le modèle PLSCanonical

Ensuite, nous utiliserons l'algorithme `PLSCanonical`, qui trouve la corrélation canonique entre deux matrices. Cet algorithme est utile lorsqu'il y a multicolinéarité entre les caractéristiques.

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### Transformez les données

Nous pouvons transformer les données d'origine à l'aide du modèle ajusté. Les données transformées auront des dimensions réduites.

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```
