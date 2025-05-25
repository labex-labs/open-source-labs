# Criar dados de teste

Primeiramente, criaremos alguns dados de teste para usar no gráfico de violino. Usaremos NumPy para gerar quatro arrays de 100 valores normalmente distribuídos com desvios padrão crescentes.

```python
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```
