# Definir los clasificadores

Definiremos dos clasificadores diferentes para comparar su rendimiento estadístico en diferentes umbrales utilizando curvas ROC y DET. Usaremos la función `make_pipeline` de scikit-learn para crear una canalización que escala los datos utilizando `StandardScaler` y entrena un clasificador `LinearSVC`. También usaremos la clase `RandomForestClassifier` de scikit-learn para entrenar un clasificador de bosque aleatorio con una profundidad máxima de 5, 10 estimadores y un máximo de 1 característica.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```
