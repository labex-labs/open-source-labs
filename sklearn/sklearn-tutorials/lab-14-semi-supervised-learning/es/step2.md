# Autoentrenamiento

#### Resumen del algoritmo de Autoentrenamiento

El algoritmo de Autoentrenamiento se basa en el algoritmo de Yarowsky. Permite que un clasificador supervisado funcione como un clasificador semi-supervisado al aprender a partir de datos no etiquetados. El algoritmo funciona entrenando iterativamente el clasificador supervisado en los datos etiquetados y no etiquetados, y luego utilizando las predicciones en los datos no etiquetados para agregar un subconjunto de estas muestras a los datos etiquetados. El algoritmo continúa iterando hasta que todas las muestras tienen etiquetas o no se seleccionan nuevas muestras en una iteración.

#### Uso del Autoentrenamiento en scikit-learn

En scikit-learn, el algoritmo de Autoentrenamiento se implementa en la clase `SelfTrainingClassifier`. Para utilizar este algoritmo, debes proporcionar un clasificador supervisado que implemente el método `predict_proba`. Aquí hay un ejemplo de cómo utilizar el algoritmo de Autoentrenamiento:

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression

# Crea un clasificador de regresión logística
classifier = LogisticRegression()

# Crea un clasificador de autoentrenamiento con el clasificador de regresión logística como clasificador base
self_training_classifier = SelfTrainingClassifier(classifier)

# Entrena el clasificador de autoentrenamiento en los datos etiquetados y no etiquetados
self_training_classifier.fit(X_labeled, y_labeled, X_unlabeled)

# Predice las etiquetas para nuevas muestras
y_pred = self_training_classifier.predict(X_test)
```

En el ejemplo anterior, `X_labeled` e `y_labeled` son los datos etiquetados, `X_unlabeled` son los datos no etiquetados y `X_test` son las nuevas muestras a predecir.
