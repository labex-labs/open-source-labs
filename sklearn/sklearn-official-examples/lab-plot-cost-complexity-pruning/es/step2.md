# Dividir los datos

Dividiremos los datos en un conjunto de entrenamiento y un conjunto de prueba.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
