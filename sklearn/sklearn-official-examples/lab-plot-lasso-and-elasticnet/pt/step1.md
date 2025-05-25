# Gerar Conjunto de Dados Sintético

Primeiro, geramos um conjunto de dados onde o número de amostras é inferior ao número total de características. Isto leva a um sistema subdeterminado, ou seja, a solução não é única e não podemos aplicar os mínimos quadrados ordinários por si só. A regularização introduz um termo de penalização na função objetivo, o que modifica o problema de otimização e pode ajudar a aliviar a natureza subdeterminada do sistema. Iremos gerar um alvo `y` que é uma combinação linear com sinais sinusoidais alternados. Apenas as 10 frequências mais baixas das 100 frequências em `X` são usadas para gerar `y`, enquanto as restantes características não são informativas. Isto resulta num espaço de características esparso de alta dimensionalidade, onde algum grau de penalização L1 é necessário.

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # tornar o coef esparso
y = np.dot(X, true_coef)

# introduzir fase aleatória usando numpy.random.random_sample
# adicionar algum ruído gaussiano usando numpy.random.normal
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# dividir os dados em conjuntos de treino e teste usando train_test_split de sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
