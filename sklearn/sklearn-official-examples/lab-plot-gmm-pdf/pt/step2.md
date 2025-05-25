# Gerar Dados

Em seguida, geraremos um conjunto de dados de mistura gaussiana com dois componentes. Criaremos um conjunto de dados gaussiano deslocado centrado em (20, 20) e um conjunto de dados gaussiano esticado centrado na origem. Em seguida, concatenaremos os dois conjuntos de dados no conjunto de treino final.

```python
n_samples = 300

# gerar amostra aleatória, dois componentes
np.random.seed(0)

# gerar dados gaussianos esféricos centrados em (20, 20)
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

# gerar dados gaussianos esticados centrados na origem
C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# concatenar os dois conjuntos de dados no conjunto de treino final
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
```
