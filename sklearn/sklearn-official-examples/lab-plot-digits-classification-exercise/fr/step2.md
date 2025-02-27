# Prétraiter les données

Nous allons ensuite prétraiter les données en mettant à l'échelle les caractéristiques dans une plage de [0, 1] en utilisant la valeur maximale des données. Cela peut être fait en divisant les données d'entrée par la valeur maximale des données d'entrée.

```python
X_digits = X_digits / X_digits.max()
```
