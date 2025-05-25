# Padronização

A padronização é uma etapa comum de pré-processamento para muitos algoritmos de aprendizado de máquina. Ela transforma os recursos para ter média zero e variância unitária. Podemos usar o `StandardScaler` do scikit-learn para realizar a padronização.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# Cria um conjunto de dados de amostra
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Inicializa o StandardScaler
scaler = StandardScaler()

# Ajusta o scaler nos dados de treinamento
scaler.fit(X)

# Transforma os dados de treinamento
X_scaled = scaler.transform(X)

# Imprime os dados transformados
print(X_scaled)
```
