# Lade den Datensatz

Wir werden den Ames Housing-Datensatz mit der `fetch_openml`-Funktion von Scikit-Learn laden und einen Teilsatz der Merkmale auswählen, um das Beispiel schneller auszuführen. Wir werden auch die kategorischen Merkmale in den Datentyp 'category' umwandeln.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(data_id=42165, as_frame=True, return_X_y=True, parser="pandas")

# Wähle nur einen Teilsatz der Merkmale von X, um das Beispiel schneller auszuführen
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
