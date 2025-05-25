# Criando Transformadores Personalizados

Em alguns casos, podemos querer converter uma função Python existente em um transformador para auxiliar na limpeza ou processamento de dados. Podemos alcançar isso usando o `FunctionTransformer` do scikit-learn.

```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

# Crie uma função personalizada
def custom_function(X):
    return np.log1p(X)

# Inicialize o FunctionTransformer
transformer = FunctionTransformer(custom_function)

# Crie um conjunto de dados de amostra
X = np.array([[0, 1],
              [2, 3]])

# Transforme os dados usando a função personalizada
X_transformed = transformer.transform(X)

# Imprima os dados transformados
print(X_transformed)
```
