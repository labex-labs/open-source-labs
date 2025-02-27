# Ajustement du réseau élastique

Nous pouvons maintenant procéder à l'ajustement. Nous devons passer la matrice de conception centrée à `fit` pour empêcher l'estimateur du réseau élastique de détecter qu'elle n'est pas centrée et de rejeter la matrice de Gram que nous avons passée. Cependant, si nous passons la matrice de conception redimensionnée, le code de prétraitement la redimensionnera incorrectement une deuxième fois. Nous passons également les poids normalisés au paramètre `sample_weight` de la fonction `fit`.

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```
