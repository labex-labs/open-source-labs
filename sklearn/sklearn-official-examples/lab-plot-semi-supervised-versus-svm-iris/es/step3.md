# Configurar los clasificadores de Auto-entrenamiento

Configuraremos dos clasificadores de Auto-entrenamiento con diferentes porcentajes de datos etiquetados: 30% y 50%. El Auto-entrenamiento es un algoritmo de aprendizaje semi-supervisado que entrena un clasificador con los datos etiquetados y luego lo utiliza para predecir las etiquetas de los datos no etiquetados. Las predicciones más confiables se agregan a los datos etiquetados y el proceso se repite hasta la convergencia.

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# Configurar los clasificadores de Auto-entrenamiento
base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
st30 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_30),
    y_30,
    "Auto-entrenamiento 30% data",
)
st50 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_50),
    y_50,
    "Auto-entrenamiento 50% data",
)
```
