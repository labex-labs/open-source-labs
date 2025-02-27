# Définir les distributions

Nous définissons une liste de différents échelleurs, transformateurs et normaliseurs pour ramener les données dans une plage prédéfinie et les stockons dans une liste appelée distributions.

```python
# Définir les distributions
distributions = [
    ("Données non mises à l'échelle", X),
    ("Données après mise à l'échelle standard", StandardScaler().fit_transform(X)),
    ("Données après mise à l'échelle min-max", MinMaxScaler().fit_transform(X)),
    ("Données après mise à l'échelle robuste", RobustScaler(quantile_range=(25, 75)).fit_transform(X)),
    ("Données après normalisation L2 par échantillon", Normalizer().fit_transform(X)),
    ("Données après transformation quantile (pdf uniforme)", QuantileTransformer(output_distribution="uniform").fit_transform(X)),
    ("Données après transformation quantile (pdf gaussienne)", QuantileTransformer(output_distribution="normal").fit_transform(X)),
    ("Données après transformation de puissance (Yeo-Johnson)", PowerTransformer(method="yeo-johnson").fit_transform(X)),
    ("Données après transformation de puissance (Box-Cox)", PowerTransformer(method="box-cox").fit_transform(X)),
]
```
