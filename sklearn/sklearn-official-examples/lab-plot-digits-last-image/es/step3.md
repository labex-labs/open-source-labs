# Preparando el conjunto de datos para el aprendizaje automático

Antes de poder entrenar un modelo de aprendizaje automático en el conjunto de datos, necesitamos preparar los datos dividiéndolos en conjuntos de entrenamiento y prueba. Esto se puede hacer utilizando la función `train_test_split` de scikit-learn:

```python
from sklearn.model_selection import train_test_split

# Divide el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```
