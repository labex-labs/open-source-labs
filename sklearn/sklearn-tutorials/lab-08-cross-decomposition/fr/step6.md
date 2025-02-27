# PLSSVD

#### Ajustez le modèle PLSSVD

L'algorithme `PLSSVD` est une version simplifiée de `PLSCanonical` qui calcule la Décomposition en Valeurs Singulières (SVD) de la matrice de covariance croisée une seule fois. Cet algorithme est utile lorsque le nombre de composantes est limité à une.

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### Transformez les données

Nous pouvons transformer les données d'origine à l'aide du modèle ajusté. Les données transformées auront des dimensions réduites.

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```
