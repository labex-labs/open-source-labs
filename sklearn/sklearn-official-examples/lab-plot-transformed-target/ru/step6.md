# Загрузите и предобработайте данные о недвижимости в Амесе

Мы загружаем набор данных о недвижимости в Амесе и предобрабатываем его, оставляя только числовые столбцы и удаляя столбцы с значениями NaN или Inf. Целевой признак, который нужно предсказать, — это цена продажи каждой квартиры.

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
