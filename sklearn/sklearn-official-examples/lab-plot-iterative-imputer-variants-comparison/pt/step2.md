# Carregar Conjunto de Dados

Carregaremos o conjunto de dados de habitação da Califórnia do Scikit-Learn. Usaremos apenas 2.000 amostras para reduzir o tempo de computação.

```python
N_SPLITS = 5

rng = np.random.RandomState(0)

X_full, y_full = fetch_california_housing(return_X_y=True)
X_full = X_full[::10]
y_full = y_full[::10]
n_samples, n_features = X_full.shape
```
