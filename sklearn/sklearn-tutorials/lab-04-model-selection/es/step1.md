# Puntuación y puntuaciones validadas cruzadas

Los estimadores en scikit-learn exponen un método `score` que se puede utilizar para evaluar la calidad de la ajuste del modelo o la predicción en nuevos datos. Este método devuelve una puntuación, donde un valor más alto indica un mejor rendimiento.

```python
from sklearn import datasets, svm

# Cargar el conjunto de datos de dígitos
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# Crear un clasificador SVM con kernel lineal
svc = svm.SVC(C=1, kernel='linear')

# Ajustar el clasificador a los datos de entrenamiento y calcular la puntuación en los datos de prueba
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

Para obtener una mejor medida de la precisión de la predicción, podemos utilizar la validación cruzada. La validación cruzada implica dividir los datos en múltiples pliegues, utilizando cada pliegue como conjunto de prueba y los pliegues restantes como conjuntos de entrenamiento. Este proceso se repite varias veces, y las puntuaciones se promedian para obtener el rendimiento general.

```python
import numpy as np

# Dividir los datos en 3 pliegues
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# Realizar la validación cruzada
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
