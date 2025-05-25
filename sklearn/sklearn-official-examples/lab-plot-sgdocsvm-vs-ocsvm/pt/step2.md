# Gerar Dados

Vamos gerar um conjunto de dados de brinquedo para este laboratório. Vamos gerar 500 amostras de treino e 20 amostras de teste. Também vamos gerar 20 amostras anormais.

```python
random_state = 42
rng = np.random.RandomState(random_state)

# Gerar dados de treino
X = 0.3 * rng.randn(500, 2)
X_train = np.r_[X + 2, X - 2]
# Gerar algumas observações regulares e novas
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# Gerar algumas observações anormais e novas
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
```
