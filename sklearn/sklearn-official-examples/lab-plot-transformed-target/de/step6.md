# Laden und Vorverarbeiten der Ames Wohnungsdaten

Wir laden den Ames Wohnungsdatensatz und verarbeiten ihn, indem wir nur numerische Spalten beibehalten und Spalten mit NaN- oder Inf-Werten entfernen. Das Ziel, das vorhergesagt werden soll, ist der Verkaufspreis jedes Hauses.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import quantile_transform

ames = fetch_openml(name="house_prices", as_frame=True, parser="pandas")

# Behalte nur numerische Spalten
X = ames.data.select_dtypes(np.number)

# Entferne Spalten mit NaN- oder Inf-Werten
X = X.drop(columns=["LotFrontage", "GarageYrBlt", "MasVnrArea"])

# Lasse den Preis in k$ liegen
y = ames.target / 1000
y_trans = quantile_transform(
    y.to_frame(), n_quantiles=900, output_distribution="normal", copy=True
).squeeze()
```
