# Cargar el conjunto de datos

Cargaremos el conjunto de datos de viviendas de Ames usando la función `fetch_openml` de Scikit-Learn y seleccionaremos un subconjunto de las características para que el ejemplo se ejecute más rápido. También convertiremos las características categóricas al tipo de datos 'category'.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(data_id=42165, as_frame=True, return_X_y=True, parser="pandas")

# Selecciona solo un subconjunto de las características de X para que el ejemplo se ejecute más rápido
categorical_columns_subset = [
    "BldgType",
    "GarageFinish",
    "LotConfig",
    "Functional",
    "MasVnrType",
    "HouseStyle",
    "FireplaceQu",
    "ExterCond",
    "ExterQual",
    "PoolQC",
]

numerical_columns_subset = [
    "3SsnPorch",
    "Fireplaces",
    "BsmtHalfBath",
    "HalfBath",
    "GarageCars",
    "TotRmsAbvGrd",
    "BsmtFinSF1",
    "BsmtFinSF2",
    "GrLivArea",
    "ScreenPorch",
]

X = X[categorical_columns_subset + numerical_columns_subset]
X[categorical_columns_subset] = X[categorical_columns_subset].astype("category")
```
