# Codificación de Características Categóricas

Las características categóricas deben ser codificadas en valores numéricos antes de poder ser utilizadas en algoritmos de aprendizaje automático. Podemos utilizar el `OrdinalEncoder` y el `OneHotEncoder` de scikit-learn para codificar las características categóricas.

```python
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import numpy as np

# Crea un conjunto de datos de muestra
X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox']]

# Inicializa el OrdinalEncoder
ordinal_encoder = OrdinalEncoder()

# Ajusta y transforma los datos de entrenamiento
X_encoded = ordinal_encoder.fit_transform(X)

# Imprime los datos transformados
print(X_encoded)

# Inicializa el OneHotEncoder
onehot_encoder = OneHotEncoder()

# Ajusta y transforma los datos de entrenamiento
X_onehot = onehot_encoder.fit_transform(X)

# Imprime los datos transformados
print(X_onehot.toarray())
```
