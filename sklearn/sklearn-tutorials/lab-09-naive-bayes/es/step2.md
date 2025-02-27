# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba

A continuación, dividiremos el conjunto de datos en conjuntos de entrenamiento y prueba utilizando la función `train_test_split` del módulo `sklearn.model_selection`. El conjunto de entrenamiento se utilizará para entrenar el clasificador Naive Bayes, y el conjunto de prueba se utilizará para evaluar su rendimiento.

```python
from sklearn.model_selection import train_test_split

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
