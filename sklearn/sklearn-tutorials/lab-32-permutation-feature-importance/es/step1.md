# Cargar el conjunto de datos

Primero, necesitamos cargar un conjunto de datos que podamos utilizar para entrenar nuestro modelo predictivo. Utilizaremos el conjunto de datos Diabetes de scikit-learn, que contiene información sobre pacientes con diabetes.

```python
from sklearn.datasets import load_diabetes

# Cargar el conjunto de datos Diabetes
diabetes = load_diabetes()

# Dividir los datos en conjuntos de entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(diabetes.data, diabetes.target, random_state=0)
```
