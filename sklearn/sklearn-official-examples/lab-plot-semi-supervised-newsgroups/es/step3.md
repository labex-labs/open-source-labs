# Entrenar y evaluar el modelo supervisado

En este paso, dividiremos el conjunto de datos en conjuntos de entrenamiento y prueba, y luego entrenaremos y evaluaremos el pipeline del modelo supervisado que creamos en el Paso 2.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Entrenar y evaluar el pipeline del modelo supervisado
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
