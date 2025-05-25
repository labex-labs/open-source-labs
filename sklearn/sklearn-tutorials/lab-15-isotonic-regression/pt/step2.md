# Criar dados de amostra

Em seguida, precisamos criar alguns dados de amostra para ajustar nosso modelo de regressão isotônica. Neste exemplo, geraremos dois arrays, `X` e `y`, representando os dados de entrada e os valores-alvo, respectivamente.

```python
import numpy as np

# Gerar dados de entrada aleatórios
np.random.seed(0)
X = np.random.rand(100)
y = 4 * X + np.random.randn(100)
```
