# Método de puntuación del Estimador

El método de puntuación del Estimador es un criterio de evaluación predeterminado proporcionado por scikit-learn para cada estimador. Calcula una puntuación que representa la calidad de las predicciones del modelo. Puede encontrar más información al respecto en la documentación de cada estimador.

A continuación, se muestra un ejemplo de uso del método `score` para un estimador:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```
