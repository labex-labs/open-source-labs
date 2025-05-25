# Gerar Dados

Neste passo, geramos um conjunto de dados aleatório com `n_samples` amostras e `n_features` características. Também adicionamos alguns valores discrepantes ao conjunto de dados.

```python
n_samples = 80
n_features = 5

# Gerar conjunto de dados aleatório
rng = np.random.RandomState(42)
X = rng.randn(n_samples, n_features)

# Adicionar valores discrepantes ao conjunto de dados
n_outliers = 20
outliers_index = rng.permutation(n_samples)[:n_outliers]
outliers_offset = 10.0 * (
    np.random.randint(2, size=(n_outliers, n_features)) - 0.5
)
X[outliers_index] += outliers_offset
```
