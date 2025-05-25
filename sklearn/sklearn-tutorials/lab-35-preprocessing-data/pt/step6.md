# Gerando Recursos Polinomiais

Às vezes, é benéfico adicionar complexidade a um modelo considerando recursos não lineares dos dados de entrada. Podemos usar o `PolynomialFeatures` do scikit-learn para gerar recursos polinomiais.

```python
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Cria um conjunto de dados de amostra
X = np.array([[0, 1],
              [2, 3],
              [4, 5]])

# Inicializa o PolynomialFeatures
poly = PolynomialFeatures(2)

# Ajusta e transforma os dados de treinamento
X_poly = poly.fit_transform(X)

# Imprime os dados transformados
print(X_poly)
```
