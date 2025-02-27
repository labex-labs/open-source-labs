# Entrenar y evaluar el modelo de Autoentrenamiento

En este paso, utilizaremos el Autoentrenamiento en el 20% de los datos etiquetados. Seleccionaremos al azar el 20% de los datos etiquetados, entrenaremos el modelo con esos datos y luego usaremos el modelo para predecir las etiquetas para el resto de los datos no etiquetados.

```python
import numpy as np

# Seleccionar el 20% de los datos de entrenamiento
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# Establecer el subconjunto no enmascarado como no etiquetado
y_train[~y_mask] = -1

# Entrenar y evaluar el pipeline de Autoentrenamiento
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
