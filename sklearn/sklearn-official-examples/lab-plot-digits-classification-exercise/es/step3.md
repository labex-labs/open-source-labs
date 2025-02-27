# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba

A continuación, dividiremos el conjunto de datos en conjuntos de entrenamiento y prueba utilizando la función `train_test_split` de scikit-learn. Utilizaremos el 90% de los datos para el entrenamiento y el 10% para la prueba.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```
