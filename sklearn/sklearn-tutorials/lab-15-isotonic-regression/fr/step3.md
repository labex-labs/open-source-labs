# Ajustez le modèle de régression isotone

Maintenant, nous pouvons ajuster le modèle de régression isotone à nos données. Nous créons une instance de la classe `IsotonicRegression` et appelons la méthode `fit` avec nos données d'entrée et nos valeurs cibles.

```python
# Ajuste le modèle de régression isotone
ir = IsotonicRegression()
ir.fit(X, y)
```
