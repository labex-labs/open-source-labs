# Limites Teóricos

O primeiro passo é explorar os limites teóricos do lema de Johnson-Lindenstrauss. Iremos plotar o número mínimo de dimensões necessárias para garantir uma incorporação `eps` para um número crescente de amostras `n_samples`. A distorção introduzida por uma projeção aleatória `p` é afirmada pelo fato de que `p` está definindo uma incorporação `eps` com boa probabilidade, como definido por:

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

Onde `u` e `v` são quaisquer linhas retiradas de um conjunto de dados com forma `(n_samples, n_features)` e `p` é uma projeção por uma matriz gaussiana aleatória `N(0, 1)` com forma `(n_components, n_features)` (ou uma matriz esparsa de Achlioptas).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# intervalo de distorções admissíveis
eps_range = np.linspace(0.1, 0.99, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# intervalo do número de amostras (observações) a serem incorporadas
n_samples_range = np.logspace(1, 9, 9)

plt.figure()
for eps, color in zip(eps_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples_range, eps=eps)
    plt.loglog(n_samples_range, min_n_components, color=color)

plt.legend([f"eps = {eps:0.1f}" for eps in eps_range], loc="lower right")
plt.xlabel("Número de observações a serem incorporadas em eps")
plt.ylabel("Número mínimo de dimensões")
plt.title("Limites de Johnson-Lindenstrauss:\nn_samples vs n_components")
plt.show()
```
