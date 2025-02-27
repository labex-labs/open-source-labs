# Dividir los datos en conjuntos de entrenamiento y prueba

Dividiremos nuestros datos en un conjunto de entrenamiento y un conjunto de prueba, con el 50% de los datos en cada conjunto.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
