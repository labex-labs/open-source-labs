# Load and preprocess Ames housing data

We load the Ames housing data set and preprocess it by keeping only numeric columns and removing columns with NaN or Inf values. The target to be predicted is the selling price of each house.

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
