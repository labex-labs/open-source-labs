# Parámetro de puntuación

Scikit-learn proporciona un parámetro `scoring` en varias herramientas de evaluación de modelos, como la validación cruzada y la búsqueda en cuadrícula. El parámetro `scoring` controla la métrica aplicada a los estimadores durante la evaluación.

A continuación, se muestra un ejemplo de uso del parámetro `scoring` con la validación cruzada:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
