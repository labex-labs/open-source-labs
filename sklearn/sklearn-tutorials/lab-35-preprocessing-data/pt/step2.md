# Escalonamento

Escalonar recursos para um intervalo específico é outra técnica comum de pré-processamento. É útil quando os recursos têm escalas diferentes e queremos trazê-los todos para um intervalo semelhante. O `MinMaxScaler` e o `MaxAbsScaler` podem ser usados para realizar o escalonamento.

```python
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
import numpy as np

# Cria um conjunto de dados de amostra
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Inicializa o MinMaxScaler
min_max_scaler = MinMaxScaler()

# Ajusta e transforma os dados de treinamento
X_minmax = min_max_scaler.fit_transform(X)

# Imprime os dados transformados
print(X_minmax)

# Inicializa o MaxAbsScaler
max_abs_scaler = MaxAbsScaler()

# Ajusta e transforma os dados de treinamento
X_maxabs = max_abs_scaler.fit_transform(X)

# Imprime os dados transformados
print(X_maxabs)
```
