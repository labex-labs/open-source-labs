# Adicionar Valores Discrepantes Fortes ao Conjunto de Dados

Vamos adicionar quatro valores discrepantes fortes ao conjunto de dados. Geraremos valores aleatórios para esses valores discrepantes usando a distribuição normal. Em seguida, adicionaremos esses valores discrepantes ao conjunto de dados.

```python
X_outliers = rng.normal(0, 0.5, size=(4, 1))
y_outliers = rng.normal(0, 2.0, size=4)
X_outliers[:2, :] += X.max() + X.mean() / 4.0
X_outliers[2:, :] += X.min() - X.mean() / 4.0
y_outliers[:2] += y.min() - y.mean() / 4.0
y_outliers[2:] += y.max() + y.mean() / 4.0
X = np.vstack((X, X_outliers))
y = np.concatenate((y, y_outliers))
```
