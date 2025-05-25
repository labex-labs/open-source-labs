# Gerar Dados Aleatórios

Vamos gerar alguns dados aleatórios para testar o nosso algoritmo. Criaremos 200 amostras com 50 características e usaremos um coeficiente verdadeiro de 3 para cada característica. Em seguida, iremos aplicar um limiar aos coeficientes para torná-los não negativos. Finalmente, adicionaremos algum ruído às amostras.

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```
