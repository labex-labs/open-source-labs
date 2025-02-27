# Évaluer les coefficients du modèle linéaire sans validation croisée

Le modèle Ridge surapprend car il attribue plus de poids à la caractéristique à cardinalité extrêmement élevée par rapport à la caractéristique informative. Exécutez le code suivant pour évaluer les coefficients du modèle linéaire sans validation croisée :

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```
