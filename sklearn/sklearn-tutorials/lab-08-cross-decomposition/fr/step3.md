# PLSRegression

#### Ajustez le modèle PLSRegression

Nous commencerons par l'algorithme `PLSRegression`, qui est une forme de régression linéaire régularisée. Nous allons ajuster le modèle à nos données.

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### Transformez les données

Nous pouvons transformer les données d'origine à l'aide du modèle ajusté. Les données transformées auront des dimensions réduites.

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```
