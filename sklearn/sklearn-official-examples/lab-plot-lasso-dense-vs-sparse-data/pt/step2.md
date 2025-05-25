# Gerar Dados Densos

Em seguida, geramos alguns dados densos que usaremos para a regressão Lasso. Usamos a função `make_regression` do Scikit-learn para gerar 200 amostras com 5000 características.

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
