# Configuração e Criação de Dados de Amostra

Antes de começarmos, vamos importar os módulos necessários e criar um DataFrame de amostra.

```python
# Importar módulos necessários
import pandas as pd
import numpy as np

# Criar um DataFrame de amostra
df = pd.DataFrame(
    {
        "a": np.random.randn(1000),
        "b": np.random.randn(1000),
        "N": np.random.randint(100, 1000, (1000)),
        "x": "x",
    }
)
df
```
