# Cargar y preprocesar los datos de la vivienda de Ames

Cargamos el conjunto de datos de la vivienda de Ames y lo preprocesamos manteniendo solo las columnas numéricas y eliminando las columnas con valores de NaN o Inf. El objetivo a predecir es el precio de venta de cada casa.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import quantile_transform

ames = fetch_openml(name="house_prices", as_frame=True, parser="pandas")

# Keep only numeric columns
X = ames.data.select_dtypes(np.number)

# Remove columns with NaN or Inf values
X = X.drop(columns=["LotFrontage", "GarageYrBlt", "MasVnrArea"])

# Let the price be in k$
y = ames.target / 1000
y_trans = quantile_transform(
    y.to_frame(), n_quantiles=900, output_distribution="normal", copy=True
).squeeze()
```
