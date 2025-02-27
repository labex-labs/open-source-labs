# Classer les caractéristiques

Après avoir ajusté les données à l'objet RFE, nous pouvons classer les caractéristiques en fonction de leur importance. Nous utiliserons l'attribut `ranking_` de l'objet RFE pour obtenir les classements des caractéristiques. Nous allons également redimensionner les classements pour qu'ils correspondent à la forme des images originales.

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```
