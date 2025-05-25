# Imputação de Valores Ausentes

Valores ausentes em um conjunto de dados podem causar problemas com algoritmos de aprendizado de máquina. Podemos usar os métodos fornecidos no módulo `impute` do scikit-learn para lidar com valores ausentes. Aqui, usaremos o `SimpleImputer` para imputar valores ausentes.

```python
from sklearn.impute import SimpleImputer
import numpy as np

# Cria um conjunto de dados de amostra com valores ausentes
X = np.array([[1., 2., np.nan],
              [3., np.nan, 5.],
              [np.nan, 4., 6.]])

# Inicializa o SimpleImputer
imputer = SimpleImputer()

# Ajusta e transforma os dados de treinamento
X_imputed = imputer.fit_transform(X)

# Imprime os dados transformados
print(X_imputed)
```
