# CCA

#### Ajustez le modèle CCA

L'algorithme `CCA` est un cas particulier de PLS et signifie Analyse de Corrélation Canonique. Il trouve la corrélation entre deux ensembles de variables.

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### Transformez les données

Nous pouvons transformer les données d'origine à l'aide du modèle ajusté. Les données transformées auront des dimensions réduites.

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```
