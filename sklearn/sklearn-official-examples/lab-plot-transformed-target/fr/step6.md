# Chargez et prétraitez les données sur le logement d'Ames

Nous chargeons l'ensemble de données sur le logement d'Ames et le prétraitons en ne conservant que les colonnes numériques et en supprimant les colonnes avec des valeurs NaN ou Inf. La cible à prédire est le prix de vente de chaque maison.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import quantile_transform

ames = fetch_openml(name="house_prices", as_frame=True, parser="pandas")

# Conservez seulement les colonnes numériques
X = ames.data.select_dtypes(np.number)

# Supprimez les colonnes avec des valeurs NaN ou Inf
X = X.drop(columns=["LotFrontage", "GarageYrBlt", "MasVnrArea"])

# Rendez le prix en k$
y = ames.target / 1000
y_trans = quantile_transform(
    y.to_frame(), n_quantiles=900, output_distribution="normal", copy=True
).squeeze()
```
