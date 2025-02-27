# Определение распределений

Мы определяем список различных масштабирующих, преобразующих и нормализующих методов, чтобы привести данные в заранее определенный диапазон и сохраняем их в списке под названием distributions.

```python
# Define distributions
distributions = [
    ("Unscaled data", X),
    ("Data after standard scaling", StandardScaler().fit_transform(X)),
    ("Data after min-max scaling", MinMaxScaler().fit_transform(X)),
    ("Data after robust scaling", RobustScaler(quantile_range=(25, 75)).fit_transform(X)),
    ("Data after sample-wise L2 normalizing", Normalizer().fit_transform(X)),
    ("Data after quantile transformation (uniform pdf)", QuantileTransformer(output_distribution="uniform").fit_transform(X)),
    ("Data after quantile transformation (gaussian pdf)", QuantileTransformer(output_distribution="normal").fit_transform(X)),
    ("Data after power transformation (Yeo-Johnson)", PowerTransformer(method="yeo-johnson").fit_transform(X)),
    ("Data after power transformation (Box-Cox)", PowerTransformer(method="box-cox").fit_transform(X)),
]
```
