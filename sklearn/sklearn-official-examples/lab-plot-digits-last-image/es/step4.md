# Entrenando un modelo de aprendizaje automático

Ahora que hemos preparado el conjunto de datos, podemos entrenar un modelo de aprendizaje automático con los datos de entrenamiento. En este ejemplo, usaremos un algoritmo de Máquina de Vectores de Soporte (SVM):

```python
from sklearn.svm import SVC

# Crea el clasificador SVM
clf = SVC(kernel='linear')

# Entrena el clasificador con los datos de entrenamiento
clf.fit(X_train, y_train)
```
