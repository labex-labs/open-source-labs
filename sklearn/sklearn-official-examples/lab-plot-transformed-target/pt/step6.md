# Carregar e pré-processar os dados de habitação de Ames

Carregamos o conjunto de dados de habitação de Ames e pré-processamos-o, mantendo apenas as colunas numéricas e removendo colunas com valores NaN ou Inf. O alvo a ser previsto é o preço de venda de cada casa.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import quantile_transform

ames = fetch_openml(name="house_prices", as_frame=True, parser="pandas")

# Manter apenas colunas numéricas
X = ames.data.select_dtypes(np.number)

# Remover colunas com valores NaN ou Inf
X = X.drop(columns=["LotFrontage", "GarageYrBlt", "MasVnrArea"])

# Deixe o preço em k$
y = ames.target / 1000
y_trans = quantile_transform(
    y.to_frame(), n_quantiles=900, output_distribution="normal", copy=True
).squeeze()
```
