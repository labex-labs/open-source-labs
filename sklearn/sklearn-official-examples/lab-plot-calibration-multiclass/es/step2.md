# Ajuste y Calibración

Entrenamos un clasificador de bosque aleatorio con 25 estimadores base (árboles) en los datos de entrenamiento y validación concatenados (1000 muestras). Este es el clasificador no calibrado.

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

Para entrenar el clasificador calibrado, comenzamos con el mismo clasificador de bosque aleatorio, pero lo entrenamos utilizando solo el subconjunto de datos de entrenamiento (600 muestras), y luego lo calibramos, con `method='sigmoid'`, utilizando el subconjunto de datos de validación (400 muestras) en un proceso de dos etapas.

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
