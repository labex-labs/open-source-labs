# Gerar Dados

Primeiro, precisamos gerar alguns dados de amostra que podemos usar para ajustar nossos modelos. Usaremos o numpy para gerar 100 amostras, cada uma com 30 características e 40 tarefas. Também selecionaremos aleatoriamente 5 características relevantes e criaremos coeficientes para elas usando ondas senoidais com frequência e fase aleatórias. Finalmente, adicionaremos algum ruído aleatório aos dados.

```python
import numpy as np

rng = np.random.RandomState(42)

# Gere alguns coeficientes 2D com ondas senoidais com frequência e fase aleatórias
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```
