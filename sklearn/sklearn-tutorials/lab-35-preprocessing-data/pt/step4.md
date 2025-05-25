# Codificação de Recursos Categóricos

Recursos categóricos precisam ser codificados em valores numéricos antes de poderem ser usados em algoritmos de aprendizado de máquina. Podemos usar o `OrdinalEncoder` e o `OneHotEncoder` do scikit-learn para codificar recursos categóricos.

```python
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import numpy as np

# Cria um conjunto de dados de amostra
X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox']]

# Inicializa o OrdinalEncoder
ordinal_encoder = OrdinalEncoder()

# Ajusta e transforma os dados de treinamento
X_encoded = ordinal_encoder.fit_transform(X)

# Imprime os dados transformados
print(X_encoded)

# Inicializa o OneHotEncoder
onehot_encoder = OneHotEncoder()

# Ajusta e transforma os dados de treinamento
X_onehot = onehot_encoder.fit_transform(X)

# Imprime os dados transformados
print(X_onehot.toarray())
```
