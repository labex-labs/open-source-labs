# Évaluer les coefficients du modèle linéaire avec validation croisée

Les coefficients du modèle linéaire montrent que la majeure partie du poids est sur la caractéristique à l'index de colonne 0, qui est la caractéristique informative. Exécutez le code suivant pour évaluer les coefficients du modèle linéaire avec validation croisée :

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```
